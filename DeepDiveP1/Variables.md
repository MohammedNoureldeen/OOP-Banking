
## ✅ Examples of Legal Identifiers
- `var`, `my_var`, `index1`, `index_1`, `_var`, `__var`, `__lt__`

---

## 📌 Conventions (Should Follow)

### 🔒 Leading Underscores
- `_my_var`:  
- **Single underscore** = internal use / system-defined names
- `__my_var`:  
- **Double underscore** = name mangling in classes (to prevent override in subclasses)

### 🧠 Dunder (Double Underscore) Methods
- `__init__`, `__str__`, `__lt__`:
- Reserved for **special use**
- **Do not invent** your own double underscore names!

### 🚫 Import Behavior
- Objects named with leading underscores (`_my_var`, `__my_var`) **won’t be imported** using:
```python
from module import *
