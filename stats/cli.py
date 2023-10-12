import os
import sys
import asyncio

path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, "%s" % path)
sys.path.insert(0, "%s/app" % path)

module_name = sys.argv[1]
argv = " ".join(sys.argv[2:])

exec("import %s" % module_name)
exec(f"asyncio.run({module_name}.{argv})")
