# Python Deep Mastery Syllabus

---

## 1. Language Semantics (Deep Level)

- **Everything is an object**: `PyObject`, `ob_refcnt`, `ob_type`, object header layout
- **Name binding vs. assignment**: namespaces, LEGB rule, `global`/`nonlocal`, closures and cell variables (`__closure__`, `cell_contents`)
- **Scoping edge cases**: class body scope, comprehension scope, late binding in closures
- **Truthiness protocol**: `__bool__`, `__len__` fallback
- Evaluation order, short-circuiting, chained comparisons, the walrus operator (`:=`)
- **Mutability, identity, interning**: small-int cache, string interning, `is` vs `==`, `sys.intern`
- **Argument passing** ("call by object reference"), `*args`/`**kwargs` unpacking rules, positional-only (`/`) and keyword-only (`*`) parameters
- **Exception machinery**: exception chaining (`__cause__`, `__context__`, `__suppress_context__`), `ExceptionGroup` and `except*`, `try/finally` return semantics, `__traceback__`

---

## 2. The Data Model (`__dunder__` Protocols)

- **Attribute access**: `__getattribute__` vs `__getattr__`, `__setattr__`, `__delattr__`, `__dir__`
- **Descriptor protocol**: `__get__`, `__set__`, `__delete__`, `__set_name__`; data vs non-data descriptors; how `property`, `classmethod`, `staticmethod`, functions, and `__slots__` are all descriptors
- Attribute lookup algorithm (the exact MRO + instance dict + descriptor precedence order)
- **Container protocols**: `__getitem__`, `__setitem__`, `__contains__`, `__iter__`, `__reversed__`, `__len__`, `__missing__`
- **Numeric protocols**: `__add__`/`__radd__`/`__iadd__`, `__index__`, `__int__`, `__float__`, `__round__`, `__matmul__`
- **Callables**: `__call__`, `__prepare__`
- **Context managers**: `__enter__`/`__exit__`, `__aenter__`/`__aexit__`, `contextlib.ExitStack`
- **Object lifecycle**: `__new__` vs `__init__`, `__del__` (and why it's dangerous), `__init_subclass__`, `__class_getitem__`
- **Hashing**: `__hash__`/`__eq__` contract, hash randomization
- **Pickling**: `__reduce__`, `__reduce_ex__`, `__getstate__`/`__setstate__`, `copyreg`
- `__slots__` internals and memory layout
- `__format__`, `__repr__` vs `__str__`, `__bytes__`, `__fspath__`

---

## 3. Type System & Object Model

- `type` is an instance of `type`; `object` and `type` circularity
- **Metaclasses**: `type.__new__`, `type.__call__`, `__prepare__`, metaclass conflicts, when to use vs `__init_subclass__`
- **MRO / C3 linearization**: the algorithm, `super()` and how it uses `__mro__`, cooperative multiple inheritance, `super()` zero-arg magic (`__class__` cell)
- **Abstract base classes**: `abc.ABCMeta`, `__subclasshook__`, virtual subclassing via `register`
- **Protocols** (structural subtyping), `typing.runtime_checkable`
- `type()` three-arg form, dynamic class creation, `types.new_class`
- Type slots (`tp_*` in C) and how dunder methods map to them
- `__class__` assignment, monkeypatching classes at runtime
- Dataclasses internals (code generation), `attrs`, `NamedTuple`, `TypedDict`
- Enum internals (`EnumMeta`)

---

## 4. Functions, Closures & Code Objects

- **Function objects**: `__code__`, `__defaults__`, `__kwdefaults__`, `__globals__`, `__closure__`, `__dict__`, `__wrapped__`
- **Code objects**: `co_code`, `co_consts`, `co_names`, `co_varnames`, `co_freevars`, `co_cellvars`, `co_flags`, `co_lnotab`/`co_lines`, `co_exceptiontable` (3.11+)
- **Decorators** (with/without args, class decorators, stacking, `functools.wraps`), decorator factories
- **`functools`**: `lru_cache`/`cache`, `singledispatch`/`singledispatchmethod`, `partial`, `partialmethod`, `cached_property`, `total_ordering`, `reduce`
- Bound vs unbound methods, `types.MethodType`, method binding at attribute access time
- Lambdas, default-argument gotchas, early vs late binding
- Recursion limits, tail-call absence, `sys.setrecursionlimit`

---

## 5. Iterators, Generators & Coroutines

- **Iterator protocol** precisely: `__iter__`/`__next__`, `StopIteration` handling, iterator exhaustion
- **Generators**: frame suspension, `send()`, `throw()`, `close()`, `GeneratorExit`, `yield` as an expression, return value in `StopIteration.value`
- `yield from` semantics (the full PEP 380 delegation algorithm)
- Generator-based pipelines, lazy evaluation, `itertools` mastery (`tee`, `groupby`, `accumulate`, `chain.from_iterable`, `islice`, `product`)
- Generator frame internals: `gi_frame`, `gi_running`, `gi_yieldfrom`, `gi_suspended`
- **Native coroutines** (`async def`), `__await__`, awaitables, `cr_frame`
- Async generators, `asend`/`athrow`, `aclose`, async comprehensions
- How `async`/`await` is generators under the hood (`CO_COROUTINE` flag, `types.coroutine`)

---

## 6. Concurrency & Parallelism

- **The GIL**: what it protects, switch interval, `sys.setswitchinterval`, I/O vs CPU-bound behavior, GIL contention
- **Free-threaded CPython** (PEP 703, `--disable-gil` / 3.13+ `t` builds): per-object locks, biased reference counting, what changes for you
- **`threading`**: `Lock`, `RLock`, `Condition`, `Semaphore`, `Event`, `Barrier`, thread-locals, daemon threads, `threading.excepthook`
- **`multiprocessing`**: fork vs spawn vs forkserver, pickling constraints, shared memory (`multiprocessing.shared_memory`), `Manager`, `Pool`, `Queue`
- **`concurrent.futures`**: `ThreadPoolExecutor`, `ProcessPoolExecutor`, `InterpreterPoolExecutor` (3.14)
- **Subinterpreters** (PEP 554/684): per-interpreter GIL, `_interpreters` / `concurrent.interpreters`
- **asyncio internals**: event loop implementation, `Future`, `Task`, `Handle`, `call_soon`, selectors, `run_in_executor`, task cancellation semantics, `TaskGroup`, `timeout`, structured concurrency, eager task factory
- Alternative loops/frameworks: `uvloop`, `trio`, `anyio`, `curio` concepts
- Memory model, atomicity of bytecode ops (what's actually atomic and what isn't), race conditions
- `contextvars` and how they propagate through tasks
- `queue`, `asyncio.Queue`, producer/consumer patterns, backpressure

---

## 7. Memory Management

- **Reference counting**: `sys.getrefcount`, `Py_INCREF`/`Py_DECREF`, borrowed vs new references, immortal objects (PEP 683)
- **Cyclic garbage collector**: generations, thresholds, `gc.collect()`, `gc.get_referrers`, `gc.get_referents`, `gc.freeze`, incremental GC (3.13/3.14), `__del__` and cycles, `gc.garbage`
- **pymalloc**: arenas, pools, blocks, small-object allocator, `PYTHONMALLOC`
- **Object size**: `sys.getsizeof`, `__sizeof__`, recursive sizing, `tracemalloc`, `pympler`, `objgraph`
- **`weakref`**: `ref`, `proxy`, `WeakValueDictionary`, `WeakKeyDictionary`, `WeakSet`, `finalize`, `__weakref__` slot
- Memory fragmentation, memory leaks in long-running processes, `mmap`
- Free lists (ints, floats, tuples, lists, dicts) and how they affect performance
- Buffer protocol and `memoryview` (zero-copy slicing), `array`, `bytearray`, `struct`
- **Copying semantics**: shallow vs deep, `copy.copy`, `copy.deepcopy`, `__copy__`/`__deepcopy__`, memo dict

---

## 8. Built-in Data Structure Internals

- **`dict`**: compact dict layout (indices + entries), open addressing, hash collision probing, insertion order guarantee, dict versioning, key-sharing (split) dicts for instances, resizing
- **`set`**: hash table, differences from dict implementation, linear probing with perturbation
- **`list`**: over-allocation growth pattern, amortized append, `sort()` = Timsort (stability, runs, galloping), `list.insert(0)` cost
- **`tuple`**: free lists, hashing algorithm (xxHash-based since 3.8)
- **`str`**: PEP 393 flexible representation (1/2/4 bytes per char), string concatenation optimization, `str.join` vs `+=`, `__str__` caching, string hashing (SipHash)
- **`int`**: arbitrary precision (30-bit digits), small-int cache (-5..256), Karatsuba multiplication, `int.bit_length`, `sys.int_info`
- **`float`**: IEEE 754, `float.hex`, `math.isclose`, `decimal`, `fractions`
- **`collections`**: `deque` (block linked list), `OrderedDict` (and why it still exists), `defaultdict`, `Counter`, `ChainMap`
- `heapq`, `bisect`, `array`, `sortedcontainers` (third-party)
- Big-O of every operation you use — with the real constants

---

## 9. Bytecode, Compiler & Interpreter

- **Compilation pipeline**: source → tokens → AST → symbol table → (CFG) → bytecode → code object
- `tokenize`, `ast` module (`ast.parse`, `ast.dump`, `ast.NodeTransformer`, `ast.unparse`, `compile()` with `ast.PyCF_ONLY_AST`)
- PEG parser (PEP 617), replacing LL(1); grammar file `Grammar/python.gram`
- `symtable` module
- **`dis` module**: reading bytecode, stack-based VM, `LOAD_FAST`/`LOAD_GLOBAL`/`LOAD_ATTR`/`CALL`/`BINARY_OP`, exception tables (zero-cost exceptions 3.11+)
- **Specializing adaptive interpreter** (PEP 659, 3.11+): quickening, superinstructions, inline caches, specialized instructions (`LOAD_ATTR_INSTANCE_VALUE`, etc.), `dis(adaptive=True)`
- `ceval.c`: the main interpreter loop, computed gotos, `_PyEval_EvalFrameDefault`
- **Frame objects**: `sys._getframe`, `f_locals`, `f_back`, `f_lineno`, interpreter frames vs Python frame objects (3.11 split), PEP 667 (`f_locals` semantics)
- Peephole optimizer and constant folding, `__debug__` and `-O`
- Experimental JIT (copy-and-patch, PEP 744, 3.13+), tier-2 micro-ops, `_Py_uop`
- `.pyc` files, importlib bytecode caching, magic numbers, `PYTHONDONTWRITEBYTECODE`
- Writing your own bytecode / code object manipulation (`types.CodeType.replace`)

---

## 10. Import System

- `import` statement → `__import__` → `importlib._bootstrap`
- **Finders and loaders**: `sys.meta_path`, `sys.path_hooks`, `sys.path_importer_cache`, `MetaPathFinder`, `PathEntryFinder`, `Loader`, `ModuleSpec`
- `__spec__`, `__loader__`, `__package__`, `__path__`, `__file__`, `__name__`
- Regular packages vs namespace packages (PEP 420)
- Relative imports, circular import mechanics and resolution
- `sys.modules` cache, module reloading (`importlib.reload`) pitfalls
- **Import hooks**: writing custom importers (e.g., importing from a zip, network, or encrypted source)
- Lazy imports (`importlib.util.LazyLoader`), `__getattr__` on modules (PEP 562), `__dir__` on modules
- Frozen modules, `zipimport`, `-m` execution (`runpy`)
- Startup sequence: `site`, `sitecustomize`, `usercustomize`, `.pth` files, `-S`, `-I`

---

## 11. Metaprogramming & Introspection

- **`inspect`**: signatures, `Parameter`, `getsource`, `getmembers`, `isgeneratorfunction`, `iscoroutinefunction`, `getclosurevars`, `unwrap`, stack inspection
- `globals()`, `locals()`, `vars()`, `dir()`, `__dict__` manipulation
- `exec`/`eval` with custom namespaces, sandboxing (and why it fundamentally doesn't work in Python)
- AST-based code generation and rewriting (how pytest rewrites asserts)
- Dynamic attribute creation, `__getattr__`-based proxies, `SimpleNamespace`
- `sys.settrace`, `sys.setprofile`, `sys.monitoring` (PEP 669, 3.12+) — how debuggers/coverage work
- `sys.excepthook`, `sys.unraisablehook`, `threading.excepthook`
- `atexit`, signal handling internals (signals only delivered in main thread between bytecodes)
- Audit hooks (`sys.addaudithook`, PEP 578)
- `codecs` and custom encodings, source encodings
- `__build_class__`, `__import__`, and other builtins you can override
- Import-time vs run-time, module-level code execution order

---

## 12. Typing System (Advanced)

- **`typing` runtime internals**: `get_type_hints`, `get_origin`, `get_args`, `Annotated`, forward references, `TYPE_CHECKING`
- **Deferred annotations** (PEP 649/749, 3.14): `annotationlib`, lazy evaluation of `__annotations__`, `__annotate__`
- **Generics**: `TypeVar` (variance, bounds, constraints), `ParamSpec`, `TypeVarTuple`, `Generic`, PEP 695 syntax (`class Foo[T]:`), `type` statement aliases
- `Protocol`, `Self`, `Literal`, `Final`, `ClassVar`, `Never`/`NoReturn`, `TypeGuard`/`TypeIs`, `Unpack`, `Required`/`NotRequired`, `ReadOnly`, `@override`, `@overload`, `@dataclass_transform`
- Callable typing, `Concatenate`, decorator typing
- **Type checkers**: `mypy`, `pyright`, `pyre`; plugin systems; strictness levels; type narrowing rules
- Runtime type validation libraries (`pydantic` v2 internals — Rust core, `beartype`, `typeguard`)
- `__class_getitem__` and `types.GenericAlias`, `types.UnionType`

---

## 13. Performance Engineering

- **Profiling**: `cProfile`, `profile`, `pstats`, `line_profiler`, `py-spy` (sampling), `scalene`, `austin`, `perf` integration (`-X perf`, 3.12+), `memray`
- `timeit` methodology, benchmark pitfalls, `pyperf`
- **Micro-optimizations that actually matter**: local variable lookup, avoiding attribute lookups in loops, `__slots__`, list comprehensions vs generators, `dict.get` vs `try/except`, string building
- Understanding what the specializing interpreter can/can't speed up
- **C extensions**: CPython C API, `Python.h`, `PyMethodDef`, `PyModuleDef`, reference counting discipline, `PyArg_ParseTuple`, GIL release (`Py_BEGIN_ALLOW_THREADS`), stable ABI / limited API (PEP 384), multi-phase init (PEP 489)
- **Cython**: `cdef`, typed memoryviews, `nogil`, annotations, pure-Python mode
- **`ctypes` and `cffi`**: calling C libraries, struct layout, callbacks, memory ownership
- PyO3 / Rust extensions, `pybind11` / `nanobind` (C++)
- `Numba` (LLVM JIT), `mypyc`, `PyPy` (tracing JIT, RPython — how it differs from CPython)
- **NumPy internals**: strides, views vs copies, broadcasting, ufuncs, `__array_interface__`, `__array_ufunc__`
- Vectorization mindset; when to escape Python entirely
- **I/O performance**: buffering, `io` hierarchy (`RawIOBase`, `BufferedIOBase`, `TextIOBase`), `os.read` vs `file.read`, `sendfile`, `os.scandir` vs `listdir`

---

## 14. CPython Source Code (Read It)

Key files to actually read in the CPython repo:

| File / Path | What it covers |
|---|---|
| `Include/object.h`, `Include/cpython/object.h` | `PyObject`, `PyTypeObject` |
| `Objects/dictobject.c`, `listobject.c`, `setobject.c`, `unicodeobject.c`, `longobject.c`, `tupleobject.c` | Core data structures |
| `Objects/typeobject.c` | `type_new`, `slot_*`, MRO, `super` |
| `Objects/funcobject.c`, `genobject.c`, `frameobject.c`, `descrobject.c` | Functions, generators, frames |
| `Objects/obmalloc.c` | pymalloc |
| `Python/ceval.c`, `Python/bytecodes.c` (DSL), `generated_cases.c.h`, `specialize.c` | Interpreter loop |
| `Python/compile.c`, `flowgraph.c`, `symtable.c`, `Parser/parser.c`, `Grammar/python.gram` | Compiler pipeline |
| `Python/import.c`, `Lib/importlib/_bootstrap.py`, `_bootstrap_external.py` | Import system |
| `Modules/gcmodule.c` / `Python/gc.c` | Garbage collector |
| `Python/pylifecycle.c`, `Python/pystate.c` | `PyThreadState`, `PyInterpreterState` |
| `Lib/asyncio/` (`base_events.py`, `tasks.py`, `futures.py`), `Modules/_asynciomodule.c` | asyncio |
| `Lib/functools.py`, `dataclasses.py`, `enum.py`, `typing.py`, `abc.py` + `Modules/_abc.c` | Standard library internals |

- Read the [Python Developer's Guide](https://devguide.python.org) and the "Internals" section
- Build CPython from source with `--with-pydebug`, use `sys.getrefcount` and `gc.get_objects` in debug mode

---

## 15. Standard Library Deep Cuts

- `sys` (everything in it), `os`, `io`, `pathlib`, `shutil`, `tempfile`
- `re` engine (backtracking, `regex` module differences, atomic groups/possessive quantifiers 3.11+)
- `struct`, `array`, `ctypes`, `mmap`, `select`/`selectors`, `socket`, `ssl`, `asyncio.streams`
- `subprocess` internals (pipes, `Popen`, deadlocks, `communicate`), `os.fork`, `os.exec*`, `pty`
- `logging` architecture (loggers, handlers, filters, formatters, `LoggerAdapter`, `QueueHandler`)
- `unittest.mock` internals (`MagicMock`, `patch`, `autospec`, spec'ing pitfalls)
- `pickle` protocols (0–5), out-of-band buffers, security; `marshal`, `shelve`, `dbm`, `json` C accelerator, `tomllib`
- `datetime`/`zoneinfo`, naive vs aware, time clocks (`monotonic`, `perf_counter`, `process_time`)
- `hashlib`, `hmac`, `secrets`, `random` (Mersenne Twister, `SystemRandom`)
- `argparse`, `dataclasses`, `enum`, `string.Template`, `textwrap`, `difflib`
- `operator`, `itertools`, `functools`, `contextlib` (`contextmanager` internals, `suppress`, `nullcontext`, `chdir`, `AsyncExitStack`)
- `warnings` (filters, `catch_warnings`, deprecation lifecycle), `traceback` (`TracebackException`, `format_exc`, fine-grained error locations PEP 657)
- `doctest`, `pdb`/`bdb` internals, `faulthandler`, `cProfile`

---

## 16. Packaging, Distribution & Toolchain

- `pyproject.toml` (PEP 517/518/621), build backends (`setuptools`, `hatchling`, `flit`, `poetry-core`, `maturin`, `scikit-build-core`)
- Wheels vs sdists, platform tags, `manylinux`/`musllinux`, ABI tags, `abi3`
- Virtual environments (`venv` internals, `pyvenv.cfg`), `uv`, pip resolver, lock files (PEP 751)
- Entry points, `importlib.metadata`, `importlib.resources`
- Editable installs (PEP 660), namespace packages in packaging
- Version specifiers (PEP 440), dependency specifiers (PEP 508), environment markers
- Reproducible builds, `pip-audit`, SBOMs, trusted publishing
- Embedding Python in C apps, `python-config`, `PyConfig` / `PyInitConfig`
- **Freezing/bundling**: `PyInstaller`, `Nuitka`, `PyOxidizer`, `zipapp`, `python -m zipapp`
- Cross-version compatibility, `__future__` imports, deprecation cycles, `python -W error`

---

## 17. Design, Architecture & Idioms

- Protocol-oriented design (duck typing formally), composition vs inheritance, mixins done right
- Design patterns as they actually look in Python (many GoF patterns dissolve into first-class functions/modules)
- Plugin architectures (entry points, `importlib`, registries via `__init_subclass__`)
- Dependency injection without frameworks
- **Immutability strategies**: `frozen=True`, `frozenset`, `MappingProxyType`, `namedtuple`
- **API design**: `__all__`, private conventions, `_` vs `__` name mangling internals, deprecation strategies
- **Error handling philosophy**: EAFP vs LBYL, exception hierarchies, custom exception design
- **Domain-specific languages in Python** (operator overloading, context managers, decorators, `__getattr__` chains — how SQLAlchemy, pandas, PyTorch build fluent APIs)
- Reading great codebases: `requests`, `attrs`, `click`, `httpx`, `trio`, `pytest`, `SQLAlchemy`, Django ORM, `numpy`, `FastAPI`/`Starlette`

---

## 18. Ecosystem Runtimes & Alternatives

- **PyPy** (meta-tracing JIT, different GC, `cpyext`), `GraalPy`, `Jython`, `IronPython`
- **MicroPython** / **CircuitPython** (constrained implementation, differences)
- **Pyodide** / WASM (Emscripten, browser Python, `pyodide.ffi`)
- **Mojo**, **Codon**, **Cinder** (Meta's fork: static Python, strict modules), **Pyston** — what they changed and why
- **RustPython**
- Understanding what is Python-the-language vs CPython-the-implementation (the language reference vs implementation details)

---

## How to Actually Study This

1. **Read the Language Reference** ([docs.python.org/3/reference](https://docs.python.org/3/reference)) cover to cover — not the tutorial. Especially "Data Model" and "Execution Model."
2. **Read the CPython source** alongside it. Use a debug build with `gdb`/`lldb` and the `python-gdb.py` helpers.
3. **Read the PEPs** for every feature you use: 8, 20, 234, 255, 302, 318, 342, 343, 380, 393, 420, 443, 484, 492, 498, 525, 526, 544, 557, 562, 570, 572, 585, 604, 617, 634–636, 646, 649, 654, 659, 673, 683, 684, 695, 701, 703, 709, 744.
4. **Books to read**:
   - *Fluent Python* — Ramalho
   - *CPython Internals* — Shaw
   - *Python in a Nutshell*
   - *High Performance Python* — Gorelick & Ozsvald
   - *Effective Python* — Slatkin
   - *Architecture Patterns with Python*
   - *Robust Python*
5. **Build these projects**:
   - A bytecode disassembler
   - A toy interpreter for a Python subset
   - A custom import hook
   - A C extension
   - An async event loop from scratch using `selectors`
   - A memory profiler using `gc` + `tracemalloc`
   - A metaclass-based ORM
   - A decorator that rewrites function ASTs
6. **Contribute to CPython** — even reading issues and PRs teaches you more than most books.