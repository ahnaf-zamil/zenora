# Copyright (c) 2021 DevGuyAhnaf

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from datetime import datetime

from .models.snowflake import *
from .models.user import *
from .models.connection import *
from .models.integration import *

from .api.userapi import *
from .api.oauthapi import *

from .impl.userapi import *
from .impl.oauthapi import *

from .client import *
from .request import *
from .utils import *
from .exceptions import *


__version__ = "0.0.2"
__author__ = "DevGuyAhnaf"
__copyright__ = f"Copyright (c) {datetime.now().strftime('%Y')} DevGuyAhnaf"
__email__ = "ahnaf@ahnafzamil.com"
__description__ = (
    "A simple to use synchronous yet functional Discord API wrapper for Python"
)
__license__ = "MIT"
__github__ = "https://github.com/ahnaf-zamil/zenora"
