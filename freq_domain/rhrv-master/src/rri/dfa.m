function [ n, fn, alpha1, alpha2, plot_data ] = dfa( t, sig, varargin )
%DFA Detrended fluctuation analysis
%   Calculates the DFA of a signal and it's scaling exponent alpha.
%   Input:
%       - t: time (or x values of signal)
%       - sig: signal data (or y values of signal)
%       - varargin: Pass in name-value pairs to configure advanced options:
%           - n_min: Minimal DFA block-size (default 4)
%           - n_max: Maximal DFA block-size (default 64)
%           - n_incr: Increment value for n (default 2)
%           - alpha1_range: Range of block size values to use for calculating the alpha1 scaling
%             exponent. Default: [4, 15].
%           - alpha2_range: Range of block size values to use for calculating the alpha2 scaling
%             exponent. Default: [16, 64].
%   Output:
%       - n: block sizes (x-axis of DFA)
%       - fn: DFA value for each block size n
%       - alpha: Exponential scaling factor
%

%% Input
DEFAULT_NMIN = rhrv_get_default('dfa.n_min', 'value');
DEFAULT_NMAX = rhrv_get_default('dfa.n_max', 'value');
DEFAULT_N_INCR = rhrv_get_default('dfa.n_incr', 'value');
DEFAULT_ALPHA1_RANGE = rhrv_get_default('dfa.alpha1_range', 'value');
DEFAULT_ALPHA2_RANGE = rhrv_get_default('dfa.alpha2_range', 'value');

% Define input
p = inputParser;
p.KeepUnmatched = true;
p.addRequired('t', @(x) isnumeric(x) && ~isscalar(x));
p.addRequired('sig', @(x) isnumeric(x) && ~isscalar(x));
p.addParameter('n_min',  DEFAULT_NMIN, @(x) isnumeric(x) && isscalar(x));
p.addParameter('n_max',  DEFAULT_NMAX, @(x) isnumeric(x) && isscalar(x));
p.addParameter('n_incr',  DEFAULT_N_INCR, @(x) isnumeric(x) && isscalar(x));
p.addParameter('alpha1_range',  DEFAULT_ALPHA1_RANGE, @(x) isnumeric(x) && numel(x) == 2);
p.addParameter('alpha2_range',  DEFAULT_ALPHA2_RANGE, @(x) isnumeric(x) && numel(x) == 2);
p.addParameter('plot', nargout == 0, @islogical);

% Get input
p.parse(t, sig, varargin{:});
n_min = p.Results.n_min;
n_max = p.Results.n_max;
n_incr = p.Results.n_incr;
alpha1_range = p.Results.alpha1_range;
alpha2_range = p.Results.alpha2_range;
should_plot = p.Results.plot;

%% DFA

% Integrate the signal without mean
nni_int = cumsum(sig - mean(sig));

N = length(nni_int);

fn = ones(n_max, 1) * NaN;
n = n_min:n_incr:n_max;

for nn = n
    % Calculate the number of windows we need for the current n
    num_win = floor(N/nn);

    % Break the signal into num_win windows of n samples each
    sig_windows = reshape(nni_int(1:nn*num_win), nn, num_win);
    t_windows  = reshape(t(1:nn*num_win), nn, num_win);
    sig_regressed = zeros(size(sig_windows));

    % Perform linear regression in each window
    for ii = 1:num_win
        y = sig_windows(:, ii);
        x = [ones(nn, 1), t_windows(:, ii)];
        b = x\y;
        yn = x * b;
        sig_regressed(:, ii) = yn;
    end

    % Calculate F(n), the value of the DFA for the current n
    fn(nn) = sqrt ( 1/N * sum((sig_windows(:) - sig_regressed(:)).^2) );
end

% Find the indices of all the DFA values we calculated
fn = fn(n);
n  = n';

%% Scaling exponent, alpha

% Find DFA values in each of the alpha ranges
alpha1_idx = find(n >= alpha1_range(1) & n <= alpha1_range(2));
alpha2_idx = find(n >= alpha2_range(1) & n <= alpha2_range(2));

% Fit a line to the log-log DFA in each alpha range
fn_log = log10(fn);
n_log = log10(n);
fit_alpha1 = polyfit(n_log(alpha1_idx), fn_log(alpha1_idx), 1);
fit_alpha2 = polyfit(n_log(alpha2_idx), fn_log(alpha2_idx), 1);

% Save the slopes of the lines
alpha1 = fit_alpha1(1);
alpha2 = fit_alpha2(1);

%% Plot
plot_data.name = 'DFA';
plot_data.n             = n;
plot_data.fn            = fn;
plot_data.alpha1_idx    = alpha1_idx;
plot_data.alpha2_idx    = alpha2_idx;
plot_data.fit_alpha1    = fit_alpha1;
plot_data.fit_alpha2    = fit_alpha2;

if should_plot
    figure('Name', plot_data.name);
    plot_dfa_fn(gca, plot_data);
end

end

