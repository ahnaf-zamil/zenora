# Zenora, a modern Python API wrapper for the Discord REST API
#
# Copyright (c) 2020 K.M Ahnaf Zamil
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from zenora.impl.rest import RESTAPI as REST
from zenora.utils.misc import print_welcome
from zenora.channels import *
from zenora.errors import *
from zenora.messages import *
from zenora.file import File
from zenora.emoji import Emoji

__author__ = "K.M Ahnaf Zamil"
__copyright__ = "© 2020 K.M Ahnaf Zamil"
__docs__ = "https://zenora-py.github.io"
__email__ = "ahnafzamil@protonmail.com"
__issue_tracker__ = "https://github.com/ahnaf-zamil/zenora/issues"
__license__ = "MIT"
__url__ = "https://github.com/ahnaf-zamil/zenora/"
__version__ = "0.0.33"
__git_sha1__ = "HEAD"


print_welcome()
