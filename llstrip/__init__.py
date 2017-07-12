# Copyright 2017 Daniel Hilst Selli
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re

class _Lstrip(object):
    def __rsub__(self, other):
        return re.sub(r'\n\s+', '\n', other)

LLSTRIP = _Lstrip()

def llstripdec(func):
    func.__doc__ = func.__doc__ - LLSTRIP
    return func

if __name__ == '__main__':
    print('''This is a indented
             multiline string. Showing
             the ability of LLSTRIP''' - LLSTRIP)

    @llstripdec
    def foo(bar):
        '''This is a docstring properly
           indented  for better readability'''
        pass

    print(foo.__doc__)
