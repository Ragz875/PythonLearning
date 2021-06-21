from fuzzywuzzy import fuzz

s1='Wilson Sonsini Goodrich & Rosati 139 Townsend St, Suite 150 San Francisco, CA 94404'
s2='Wilson Sonsini Goodrich & Rosati 139 Townsend Street, Suite 150 San Francisco CA'

s11='Wilson Sonsini Goodrich  Rosati 139 Townsend Street Suite 150 San Francisco CA 94404'
s22='Wilson Sonsini Goodrich  Rosati 139 Townsend Street Suite 150 San Francisco CA'

print("FuzzyWuzzy Ratio: s1 vs s2", fuzz.ratio(s1, s2))
print("FuzzyWuzzy PartialRatio: s1 vs s2", fuzz.partial_ratio(s1, s2))

print("FuzzyWuzzy Ratio: s11 vs s22", fuzz.ratio(s11, s22))
print("FuzzyWuzzy PartialRatio: s11 vs s22", fuzz.partial_ratio(s11, s22))