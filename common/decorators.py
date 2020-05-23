import cProfile
import tempfile
import pstats


def profile(sort="tottime", lines=50, strip_dirs=False):
    def decorator(fun):
        def inner(*args, **kwargs):
            file = tempfile.NamedTemporaryFile()
            pr = cProfile.Profile()

            try:
                result = pr.runcall(fun, *args, **kwargs)
            except Exception as e:
                file.close()
                raise e

            pr.dump_stats(file.name)
            stats = pstats.Stats(file.name)

            if strip_dirs:
                stats.strip_dirs()

            if isinstance(sort, (tuple, list)):
                stats.sort_stats(*sort)
            else:
                stats.sort_stats(sort)
            stats.print_stats(lines)

            file.close()

            return result

        return inner

    if hasattr(sort, "__call__"):
        fun = sort
        sort = "tottime"
        decorator = decorator(fun)
    return decorator
