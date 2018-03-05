#!/usr/bin/env python
# Copyright 2018 Paulocracy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import tkinter
import webbrowser

from submodules.p_markup import PMarkup
from submodules.directory_selection import DirectorySelection


class PMarkupGUI(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("P-Markup")

        self.input_folder = DirectorySelection(self, "Select the input folder:", "./Input_Example")
        self.output_folder = DirectorySelection(self, "Select the output folder:", "./Output_Example")
        self.button = tkinter.Button(self, text="Run", command=self._run)

        self.input_folder.pack()
        self.output_folder.pack()
        self.button.pack()
        
        self.mainloop()
    
    def _run(self, *e):
        PMarkup(self.input_folder.get(), self.output_folder.get())


def main(args):
    PMarkupGUI()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
