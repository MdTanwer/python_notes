# These all feel different syntactically...
x = 42
def f(): pass
class C: pass

# ...but structurally they're the same thing: objects
print(type(x))    # <class 'int'>
print(type(f))    # <class 'function'>
print(type(C))    # <class 'type'>
print(type(type)) # <class 'type'>   ← even the type of types is a type