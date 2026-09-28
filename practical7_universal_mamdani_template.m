%% UNIVERSAL MAMDANI FUZZY LOGIC TEMPLATE (NO FUZZY LOGIC TOOLBOX)
% Practical 7 - Washing Time example
%
% HOW TO USE:
% 1. Change ONLY the sections marked "CHANGE HERE" when the question changes.
% 2. Save this file as practical7_universal.m and press Run.
% 3. This script uses basic MATLAB code; no Fuzzy Logic Toolbox is required.
%
% IMPORTANT:
% - This template uses triangular membership functions (trimf).
% - The rule table contains output MF numbers:
%       1 = Very Small, 2 = Small, 3 = Medium, 4 = Large, 5 = Very Large
% - The current rule table is a suggested example for washing time.
% - Make sure every input's MF count matches the rule table dimensions.

clc;
clear;
close all;

%% ===================== CHANGE HERE: 1. INPUT VALUES =====================
% Enter the test values given in the question.
dirt = 70;       % CHANGE: input 1 value
grease = 40;     % CHANGE: input 2 value

%% ============== CHANGE HERE: 2. INPUT MEMBERSHIP FUNCTIONS ===============
% Each row is [a b c] for one triangular membership function.
% Rows are ordered: Small, Medium, Large.
% Change the ranges/parameters if the question gives different values.

dirtMF = [  0   0  50;     % Small
            0  50 100;     % Medium
           50 100 100];    % Large

greaseMF = [  0   0  50;   % Small
              0  50 100;   % Medium
             50 100 100];  % Large

% CHANGE if the question uses different names or number of fuzzy sets.
dirtNames = {'Small','Medium','Large'};
greaseNames = {'Small','Medium','Large'};

%% ============== CHANGE HERE: 3. OUTPUT MEMBERSHIP FUNCTIONS ==============
% Each row is [a b c] for one output triangular membership function.
% Current order: Very Small, Small, Medium, Large, Very Large.

washMF = [  0   0 10;      % 1 = Very Small
            0  10 25;      % 2 = Small
           10  25 40;      % 3 = Medium
           25  40 60;      % 4 = Large
           40  60 60];     % 5 = Very Large

outputNames = {'Very Small','Small','Medium','Large','Very Large'};

% CHANGE: output universe/range according to your question.
outputMin = 0;
outputMax = 60;

%% ================= CHANGE HERE: 4. FUZZY RULE TABLE =====================
% Rows = input 1 sets (Small, Medium, Large)
% Columns = input 2 sets (Small, Medium, Large)
% Each number is the selected output MF row number (1 to 5).
%
% Current suggested rules:
%                    Grease: Small  Medium  Large
% Dirt: Small             1       2      3
% Dirt: Medium            2       3      4
% Dirt: Large             3       4      5

rules = [1 2 3;
         2 3 4;
         3 4 5];

%% =================== 5. FUZZIFICATION (KEEP AS IS) ======================
% Calculate how strongly each input belongs to each fuzzy set.

dirtLevel = zeros(1, size(dirtMF,1));
greaseLevel = zeros(1, size(greaseMF,1));

for i = 1:size(dirtMF,1)
    dirtLevel(i) = trimf_custom(dirt, dirtMF(i,:));
end

for j = 1:size(greaseMF,1)
    greaseLevel(j) = trimf_custom(grease, greaseMF(j,:));
end

%% ================== 6. OUTPUT UNIVERSE (KEEP AS IS) =====================
x = linspace(outputMin, outputMax, 601);
aggregated = zeros(size(x));

%% =================== 7. FUZZY INFERENCE (KEEP AS IS) ====================
% Mamdani AND = minimum; combine rule outputs = maximum.
% Each rule clips its output membership function at its firing strength.

for i = 1:size(dirtMF,1)
    for j = 1:size(greaseMF,1)

        strength = min(dirtLevel(i), greaseLevel(j));
        outputIndex = rules(i,j);

        outputMF = arrayfun(@(v) ...
            trimf_custom(v, washMF(outputIndex,:)), x);

        clippedMF = min(strength, outputMF);
        aggregated = max(aggregated, clippedMF);
    end
end

%% ================== 8. DEFUZZIFICATION (KEEP AS IS) =====================
% Centroid method: weighted center of the aggregated output area.

areaUnderCurve = sum(aggregated);

if areaUnderCurve == 0
    washTime = NaN;
    warning('No rule fired. Check input ranges, membership functions, and rules.');
else
    washTime = sum(x .* aggregated) / areaUnderCurve;
end

%% ===================== 9. DISPLAY RESULTS ===============================
fprintf('\n----- Mamdani Fuzzy System Result -----\n');
fprintf('Input 1 (Dirt Level): %g\n', dirt);
fprintf('Input 2 (Grease Level): %g\n', grease);
fprintf('Calculated output: %.2f minutes\n', washTime);

fprintf('\nDirt memberships:\n');
for i = 1:numel(dirtLevel)
    fprintf('  %s = %.3f\n', dirtNames{i}, dirtLevel(i));
end

fprintf('\nGrease memberships:\n');
for j = 1:numel(greaseLevel)
    fprintf('  %s = %.3f\n', greaseNames{j}, greaseLevel(j));
end

%% ========================= 10. PLOT OUTPUT ===============================
figure;
plot(x, aggregated, 'LineWidth', 2);
xlabel('Washing Time (minutes)');
ylabel('Membership Degree');
title('Mamdani Fuzzy Logic - Aggregated Output');
xlim([outputMin outputMax]);
ylim([0 1.05]);
grid on;

%% =================== LOCAL FUNCTION (KEEP AS IS) ========================
% Triangular membership function with support for shoulder triangles.
function y = trimf_custom(x, p)
    a = p(1);
    b = p(2);
    c = p(3);

    if x < a || x > c
        y = 0;
    elseif x == b
        y = 1;
    elseif x < b
        if a == b
            y = 1;
        else
            y = (x-a)/(b-a);
        end
    else
        if b == c
            y = 1;
        else
            y = (c-x)/(c-b);
        end
    end
end
