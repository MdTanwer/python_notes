# Python Deep Mastery Syllabus
 20/09/2026 target 30/09/2026
             
---

## PHASE 1: Language Semantics (Deep Foundation)

- **Everything is an object**: `PyObject`, `ob_refcnt`, `ob_type`, object header layout
- **Name binding vs assignment**: namespaces, LEGB rule, `global`/`nonlocal`
- **Closures & cell variables**: `__closure__`, `cell_contents`, early vs late binding
- **Scoping edge cases**: class body scope, comprehension scope, late-binding gotchas
- **Truthiness protocol**: `__bool__`, `__len__` fallback
- **Evaluation semantics**: evaluation order, short-circuiting, chained comparisons, walrus operator (`:=`)
- **Mutability, identity, interning**: small-int cache (-5..256), string interning, `is` vs `==`, `sys.intern`
- **Argument passing**: call-by-object-reference, `*args`/`**kwargs` unpacking rules, positional-only (`/`), keyword-only (`*`)
- **Exception machinery**: chaining (`__cause__`, `__context__`, `__suppress_context__`), `ExceptionGroup` + `except*`, `try/finally` return semantics, `__traceback__`, exception notes (3.11+)

---

## PHASE 2: The Data Model (Dunder Protocols)

- **Attribute access**: `__getattribute__` vs `__getattr__`, `__setattr__`, `__delattr__`, `__dir__`
- **Descriptor protocol**: `__get__`/`__set__`/`__delete__`/`__set_name__`; data vs non-data descriptors; how `property`, `classmethod`, `staticmethod`, functions, and `__slots__` are all descriptors
- **Attribute lookup algorithm**: exact MRO + instance dict + descriptor precedence order
- **Container protocols**: `__getitem__`, `__setitem__`, `__contains__`, `__iter__`, `__reversed__`, `__len__`, `__missing__`
- **Numeric protocols**: `__add__`/`__radd__`/`__iadd__`, `__index__`, `__int__`, `__float__`, `__round__`, `__matmul__`
- **Callables**: `__call__`, `__prepare__`
- **Context managers**: `__enter__`/`__exit__`, `__aenter__`/`__aexit__`, `contextlib` (`ExitStack`, `contextmanager`, `suppress`, `redirect_stdout`)
- **Object lifecycle**: `__new__` vs `__init__`, `__del__` (and why it's dangerous), `__init_subclass__`, `__class_getitem__`
- **Hashing**: `__hash__`/`__eq__` contract, hash randomization (`PYTHONHASHSEED`)
- **Pickling & copying**: `__reduce__`, `__reduce_ex__`, `__getstate__`/`__setstate__`, `copyreg`, `__copy__`/`__deepcopy__`, memo dict
- **`__slots__` internals**: memory layout, member descriptors, inheritance pitfalls
- **Representation protocols**: `__format__`, `__repr__` vs `__str__`, `__bytes__`, `__fspath__`

---

## PHASE 3: Type System & Object Model

- **The type/object circularity**: `type` is an instance of itself
- **Metaclasses**: `type.__new__`, `type.__call__`, `__prepare__`, metaclass conflicts
- **Metaclass vs `__init_subclass__`**: decision framework for which to use
- **MRO & C3 linearization**: the algorithm, `super()` internals via `__mro__`, cooperative multiple inheritance, zero-arg `super()` magic (`__class__` cell)
- **Abstract base classes**: `abc.ABCMeta`, `__subclasshook__`, virtual subclassing via `register`
- **Protocols (structural subtyping)**: `typing.runtime_checkable`
- **Dynamic class creation**: `type()` three-arg form, `types.new_class`, `__build_class__`
- **Type slots (`tp_*` in C)**: how dunder methods map to C-level slots
- **Runtime class mutation**: `__class__` assignment, monkeypatching classes
- **Dataclasses internals**: code generation, `attrs`, `NamedTuple`, `TypedDict` comparison
- **Mixins**: cooperative mixins, mixin vs ABC vs Protocol, `super()` in mixins, Django-style mixin patterns
- **Enum internals**: `EnumMeta`, member creation, `_generate_next_value_`

---

## PHASE 4: Functions, Closures & Code Objects

- **Function objects**: `__code__`, `__defaults__`, `__kwdefaults__`, `__globals__`, `__closure__`, `__dict__`, `__wrapped__`
- **Code objects**: `co_code`, `co_consts`, `co_names`, `co_varnames`, `co_freevars`, `co_cellvars`, `co_flags`, `co_lines`, `co_exceptiontable` (3.11+)
- **Decorators (complete)**: with/without args, class decorators, stacking, decorator factories, `functools.wraps` internals
- **`functools` mastery**: `lru_cache`/`cache`, `singledispatch`/`singledispatchmethod`, `partial`, `partialmethod`, `cached_property`, `total_ordering`, `reduce`
- **Currying**: manual currying, `partial` as currying tool, `toolz.curry`, currying vs partial application
- **Bound vs unbound methods**: `types.MethodType`, method binding at attribute-access time
- **Lambda & default-arg gotchas**: early vs late binding, mutable defaults
- **Recursion**: recursion limits, absence of tail-call optimization, `sys.setrecursionlimit`

---

## PHASE 5: Iterators, Generators & Coroutines

- **Iterator protocol (precise)**: `__iter__`/`__next__`, `StopIteration` handling, exhaustion semantics
- **Generators**: frame suspension, `send()`, `throw()`, `close()`, `GeneratorExit`, `yield` as expression, return value in `StopIteration.value`
- **`yield from` semantics**: the full PEP 380 delegation algorithm
- **Generator pipelines**: lazy evaluation, `itertools` mastery (`tee`, `groupby`, `accumulate`, `chain.from_iterable`, `islice`, `product`, `pairwise`, `batched`)
- **Generator frame internals**: `gi_frame`, `gi_running`, `gi_yieldfrom`, `gi_suspended`
- **Native coroutines**: `async def`, `__await__`, awaitables, `cr_frame`
- **Async generators**: `asend`/`athrow`/`aclose`, async comprehensions
- **Coroutines = generators**: `CO_COROUTINE` flag, `types.coroutine`, the historical evolution

---

## PHASE 6: Built-in Data Structure Internals

- **`dict`**: compact layout (indices + entries), open addressing, collision probing, insertion order, dict versioning, key-sharing (split) dicts, resizing
- **`set`**: hash table vs dict implementation, linear probing with perturbation
- **`list`**: over-allocation growth pattern, amortized append, Timsort (stability, runs, galloping), `insert(0)` cost
- **`tuple`**: free lists, hashing algorithm (xxHash since 3.8)
- **`str`**: PEP 393 flexible representation (1/2/4 bytes per char), concatenation optimization, `join` vs `+=`, SipHash
- **`int`**: arbitrary precision (30-bit digits), small-int cache, Karatsuba multiplication, `sys.int_info`
- **`float`**: IEEE 754, `float.hex`, `math.isclose`, `decimal`, `fractions`
- **`collections` internals**: `deque` (block linked list), `OrderedDict` (why it still exists), `defaultdict`, `Counter`, `ChainMap`
- **`namedtuple` internals**: class generation via `exec`, `_make`, `_replace`, `_asdict`, vs `NamedTuple` vs `dataclass` (memory & speed)
- **Specialized structures**: `heapq`, `bisect`, `array`, third-party `sortedcontainers`
- **True Big-O**: every operation with real constants, not just asymptotics

---

## PHASE 7: Memory Management

- **Reference counting**: `sys.getrefcount`, `Py_INCREF`/`Py_DECREF`, borrowed vs new references, immortal objects (PEP 683)
- **Cyclic GC**: generations, thresholds, `gc.collect()`, `gc.get_referrers`, `gc.freeze`, incremental GC (3.14), `__del__` + cycles, `gc.garbage`
- **pymalloc**: arenas, pools, blocks, small-object allocator, `PYTHONMALLOC`
- **Measuring memory**: `sys.getsizeof`, `__sizeof__`, `tracemalloc`, `pympler`, `objgraph`
- **`weakref`**: `ref`, `proxy`, `WeakValueDictionary`, `WeakKeyDictionary`, `WeakSet`, `finalize`, `__weakref__` slot
- **Long-running processes**: fragmentation, leak hunting, `mmap`
- **Free lists**: ints, floats, tuples, lists, dicts and their performance impact
- **Buffer protocol**: `memoryview` (zero-copy slicing), `array`, `bytearray`, `struct`

---

## PHASE 8: Bytecode, Compiler & Interpreter

- **Compilation pipeline**: source -> tokens -> AST -> symbol table -> CFG -> bytecode -> code object
- **`tokenize` & `ast` modules**: `ast.parse`, `ast.dump`, `ast.NodeTransformer`, `ast.unparse`, `compile()` with `PyCF_ONLY_AST`
- **PEG parser (PEP 617)**: replaced LL(1); `Grammar/python.gram`
- **`symtable` module**
- **`dis` module**: stack-based VM, `LOAD_FAST`/`LOAD_GLOBAL`/`CALL`/`BINARY_OP`, exception tables (zero-cost exceptions 3.11+)
- **Specializing adaptive interpreter (PEP 659)**: quickening, inline caches, specialized instructions, `dis(adaptive=True)`
- **`ceval.c`**: main interpreter loop, computed gotos, `_PyEval_EvalFrameDefault`
- **Frame objects**: `sys._getframe`, `f_locals`, `f_back`, interpreter frames vs Python frames (3.11 split), PEP 667
- **Peephole optimizer**: constant folding, `__debug__`, `-O` flag
- **JIT (PEP 744, 3.13+)**: copy-and-patch, tier-2 micro-ops (`_Py_uop`)
- **`.pyc` files**: bytecode caching, magic numbers, `PYTHONDONTWRITEBYTECODE`, `types.CodeType.replace`

---

## PHASE 9: Import System

- **Import pipeline**: `import` -> `__import__` -> `importlib._bootstrap`
- **Finders & loaders**: `sys.meta_path`, `sys.path_hooks`, `MetaPathFinder`, `Loader`, `ModuleSpec`
- **Module attributes**: `__spec__`, `__loader__`, `__package__`, `__path__`, `__file__`, `__name__`
- **Packages**: regular vs namespace packages (PEP 420)
- **Relative imports & circular imports**: mechanics and resolution strategies
- **`sys.modules` cache**: `importlib.reload` pitfalls
- **Custom importers**: importing from zip/network/encrypted sources
- **Lazy imports**: `importlib.util.LazyLoader`, module `__getattr__` (PEP 562), module `__dir__`
- Frozen modules, `zipimport`, `-m` execution (`runpy`)
- **Startup sequence**: `site`, `sitecustomize`, `usercustomize`, `.pth` files, `-S`, `-I` flags

---

## PHASE 10: Metaprogramming & Introspection

- **`inspect` module**: `Signature`, `Parameter`, `getsource`, `getclosurevars`, `unwrap`, stack inspection
- **Namespace manipulation**: `globals()`, `locals()`, `vars()`, `__dict__` hacking
- **`exec`/`eval`**: custom namespaces, why sandboxing fundamentally fails in Python
- **AST code rewriting**: how pytest rewrites `assert` statements
- **Dynamic proxies**: `__getattr__`-based proxies, `SimpleNamespace`
- **Tracing & profiling hooks**: `sys.settrace`, `sys.setprofile`, `sys.monitoring` (PEP 669, 3.12+) -- how debuggers and coverage.py work
- **Error hooks**: `sys.excepthook`, `sys.unraisablehook`, `threading.excepthook`
- **`atexit` & signal internals**: signals delivered only in main thread between bytecodes
- **Audit hooks (PEP 578)**: `sys.addaudithook`
- **`codecs`**: custom encodings, source encodings

---

## PHASE 11: Concurrency & Parallelism

- **The GIL (complete)**: what it protects, switch interval, I/O vs CPU-bound behavior, contention
- **Free-threaded CPython (PEP 703, 3.13t+)**: per-object locks, biased reference counting, practical implications
- **`threading`**: `Lock`, `RLock`, `Condition`, `Semaphore`, `Event`, `Barrier`, thread-locals, daemon threads
- **`multiprocessing`**: fork vs spawn vs forkserver, pickling constraints, `shared_memory`, `Manager`, `Pool`
- **`concurrent.futures`**: `ThreadPoolExecutor`, `ProcessPoolExecutor`, `InterpreterPoolExecutor` (3.14)
- **Subinterpreters (PEP 554/684)**: per-interpreter GIL, `concurrent.interpreters`
- **asyncio internals**: event loop implementation, `Future`, `Task`, `Handle`, `call_soon`, selectors, cancellation semantics, `TaskGroup`, structured concurrency, eager task factory
- **Alternative frameworks**: `uvloop`, `trio`, `anyio`, `curio` concepts
- **Memory model**: atomicity of bytecode ops, race conditions
- **`contextvars`**: propagation through tasks
- **Queue patterns**: `queue`, `asyncio.Queue`, producer/consumer, backpressure
- **Building a custom event loop**: mini-asyncio from generators + selectors; how curio/trio reimagine the loop
- **Async ecosystem**: `aiohttp`/`httpx`, connection pooling, async DB drivers

---

## PHASE 12: Typing System (Advanced)

- **Typing runtime internals**: `get_type_hints`, `get_origin`, `get_args`, `Annotated`, forward references, `TYPE_CHECKING`
- **Deferred annotations (PEP 649/749, 3.14)**: `annotationlib`, `__annotate__`
- **Generics**: `TypeVar` (variance/bounds/constraints), `ParamSpec`, `TypeVarTuple`, PEP 695 syntax (`class Foo[T]`), `type` statement
- **Special forms**: `Protocol`, `Self`, `Literal`, `Final`, `Never`, `TypeGuard`/`TypeIs`, `Unpack`, `@override`, `@overload`, `@dataclass_transform`
- **Callable typing**: `Concatenate`, typing decorators correctly
- **Type checkers**: `mypy`, `pyright`, plugin systems, strictness, type narrowing
- **Runtime validation**: `pydantic` v2 internals (Rust core), `beartype`, `typeguard`
- **Generic aliases**: `__class_getitem__`, `types.GenericAlias`, `types.UnionType`

---

## PHASE 12.5: Design Patterns (Pythonic Implementation)

- **Creational**: Singleton (metaclass vs decorator vs module vs `__new__`), Factory, Abstract Factory, Builder
- **Structural**: Adapter, Facade, Proxy (via `__getattr__`), Decorator pattern vs decorators
- **Behavioral**: Observer, Strategy, Command, Template Method, Chain of Responsibility
- **Patterns that vanish in Python**: Strategy = first-class functions, Iterator = generators, dependency injection, Registry pattern via `__init_subclass__`

---

## PHASE 13: Performance Engineering

- **Profiling**: `cProfile`, `pstats`, `line_profiler`, `py-spy` (sampling), `scalene`, `-X perf` (3.12+), `memray`
- **Benchmarking**: `timeit` methodology, pitfalls, `pyperf`
- **Micro-optimizations that matter**: local lookups, attribute caching, `__slots__`, comprehension vs generator, `dict.get` vs `try/except`
- What the specializing interpreter can/can't speed up
- **C extensions**: CPython C API, `PyMethodDef`, refcount discipline, `Py_BEGIN_ALLOW_THREADS`, stable ABI (PEP 384), multi-phase init (PEP 489)
- **Cython**: `cdef`, typed memoryviews, `nogil`, pure-Python mode
- **`ctypes` & `cffi`**: C library calls, struct layout, callbacks, memory ownership
- **Rust/C++ extensions**: PyO3 + maturin, `pybind11`, `nanobind`
- **Alternative runtimes**: Numba (LLVM JIT), `mypyc`, PyPy (tracing JIT vs CPython)
- **NumPy internals**: strides, views vs copies, broadcasting, ufuncs, `__array_ufunc__`
- **I/O performance**: `io` hierarchy (`RawIOBase` -> `BufferedIOBase` -> `TextIOBase`), `os.read` vs `file.read`, `sendfile`, `os.scandir`
- **Vectorization mindset**: when to escape Python entirely

---

## PHASE 14: Metaprogramming Frameworks & DSLs

- **Build your own framework**: metaclasses + descriptors + `__init_subclass__` + decorators combined; how Django ORM / SQLAlchemy declarative works internally
- **Building DSLs**: operator overloading for fluent APIs, `__getitem__` trickery (`User.name == "x"` SQLAlchemy-style), context-manager DSLs, AST-based DSLs

---

## PHASE 15: Building Compilers & Interpreters

- **Mini-interpreter project**: tokenizer -> parser -> AST -> evaluator for a small language
- **Compiling to Python bytecode**: generating `CodeType` objects directly
- **Source-to-source transpilation**: AST-to-AST transforms (macros, py2to3-style tools)

---

## PHASE 16: Distributed Python

- **Celery**: task queues, brokers (Redis/RabbitMQ), workers, beat, retries, pickling constraints
- **Dask**: lazy task graphs, distributed scheduler, DataFrames at scale
- **Ray**: actors, remote functions, object store, cluster computing

---
---

## Standard Library Deep Cuts

- `sys` (everything in it), `os`, `io`, `pathlib`, `shutil`, `tempfile`
- `re` engine (backtracking, `regex` module differences, atomic groups/possessive quantifiers 3.11+)
- `struct`, `array`, `ctypes`, `mmap`, `select`/`selectors`, `socket`, `ssl`, `asyncio.streams`
- `subprocess` internals (pipes, `Popen`, deadlocks, `communicate`), `os.fork`, `os.exec*`, `pty`
- `logging` architecture (loggers, handlers, filters, formatters, `LoggerAdapter`, `QueueHandler`)
- `unittest.mock` internals (`MagicMock`, `patch`, `autospec`, spec pitfalls)
- `pickle` protocols (0-5), out-of-band buffers, security; `marshal`, `shelve`, `dbm`, `json` C accelerator, `tomllib`
- `datetime`/`zoneinfo`, naive vs aware, time clocks (`monotonic`, `perf_counter`, `process_time`)
- `hashlib`, `hmac`, `secrets`, `random` (Mersenne Twister, `SystemRandom`)
- `argparse`, `dataclasses`, `enum`, `string.Template`, `textwrap`, `difflib`
- `operator`, `itertools`, `functools`, `contextlib` (`contextmanager` internals, `suppress`, `nullcontext`, `chdir`, `AsyncExitStack`)
- `warnings` (filters, `catch_warnings`, deprecation lifecycle), `traceback` (`TracebackException`, `format_exc`, fine-grained error locations PEP 657)
- `doctest`, `pdb`/`bdb` internals, `faulthandler`, `cProfile`

---

## Packaging, Distribution & Toolchain

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

## Ecosystem Runtimes & Alternatives

- **PyPy** (meta-tracing JIT, different GC, `cpyext`), `GraalPy`, `Jython`, `IronPython`
- **MicroPython** / **CircuitPython** (constrained implementation, differences)
- **Pyodide** / WASM (Emscripten, browser Python, `pyodide.ffi`)
- **Mojo**, **Codon**, **Cinder** (Meta fork: static Python, strict modules), **Pyston** -- what they changed and why
- **RustPython**
- Understanding what is Python-the-language vs CPython-the-implementation (the language reference vs implementation details)

---

## Design, Architecture & Idioms

- Protocol-oriented design (duck typing formally), composition vs inheritance, mixins done right
- Design patterns as they actually look in Python (many GoF patterns dissolve into first-class functions/modules)
- Plugin architectures (entry points, `importlib`, registries via `__init_subclass__`)
- Dependency injection without frameworks
- **Immutability strategies**: `frozen=True`, `frozenset`, `MappingProxyType`, `namedtuple`
- **API design**: `__all__`, private conventions, `_` vs `__` name mangling internals, deprecation strategies
- **Error handling philosophy**: EAFP vs LBYL, exception hierarchies, custom exception design
- **Domain-specific languages in Python** (operator overloading, context managers, decorators, `__getattr__` chains -- how SQLAlchemy, pandas, PyTorch build fluent APIs)
- Reading great codebases: `requests`, `attrs`, `click`, `httpx`, `trio`, `pytest`, `SQLAlchemy`, Django ORM, `numpy`, `FastAPI`/`Starlette`

---
