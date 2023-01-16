# MODULARIZATION -- Modules
# => Modularization is a practice of organizing codebase into loosely coupled and self-contained parts;
# Each part is a module. Each module is independent and serves a clear purpose

from exe_modules import factorial, double, triple  # Not recommended
# or
import exe_modules  # Recommended

print(factorial(3))
print(exe_modules.double(4))
print(double(7))
print(triple(9))

# Advantages of modularization

# => Code organization
# => Ease of maintenance
# => Detailed code hiding
# Reuse in other projects
