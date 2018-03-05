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

from distutils.dir_util import copy_tree
import glob
import sys


class MarkupFile:
    def __init__(self):
        self.html_header = "<!DOCTYPE html>\n"\
                           "<html>\n"
        self.script = "<head>\n"\
                      "<meta http-equiv='Content-Type' content='text/html' charset='utf-8'>\n"\
                      "<style>\n"\
                      "img { max-width: 100%; height: auto; width: auto; }\n"\
                      "</style>\n"\
                      "<script>"
        self.body = "<body>"
        self.function_counter = 0
        self.variables = {}

        self.commands = {"IMG":self._add_img,
                         "INPUTSTRING":self._add_inputstring,
                         "INPUTNUMBER":self._add_inputnumber,
                         "LINK":self._add_link,
                         "REM":self._add_rem,
                         "SCRIPTBUTTON":self._add_scriptbutton,
                         "SET":self._add_set,
                         "VIDEO":self._add_video}

    def _add_img(self, arguments):
        self.body += "<img src='"+arguments+"'>"

    def _add_inputnumber(self, arguments):
        var_name = arguments.split(" ")[0]
        function_name = "_"+str(self.function_counter)
        self.function_counter += 1

        self.script += "function "+function_name+"(event){\n"
        self.script += var_name +"=parseFloat(event.value);\n"
        self.script += "}\n"

        input_ = "<input type='number' step='any' oninput='"+function_name+"(this)' value='"+self.variables[var_name]+"'>\n"

        self.body += input_

    def _add_inputstring(self, arguments):
        var_name = arguments.split(" ")[0]
        function_name = "_"+str(self.function_counter)
        self.function_counter += 1

        self.script += "function "+function_name+"(event){\n"
        self.script += var_name +"=event.value;\n"
        self.script += "}\n"

        input_ = "<input type='text' oninput='"+function_name+"(this)' value='"+self.variables[var_name]+"'>\n"

        self.body += input_

    def _add_link(self, arguments):
        path = arguments.split(" ")[0]
        text = arguments[len(path):]

        self.body += "<a href='"+path+"'>"+text+"</a>"

    def _add_rem(self, arguments):
        pass

    def _add_scriptbutton(self, arguments):
        text = arguments.split("\n")[0]
        function_code = arguments[len(text):]
        
        id_name = "_"+str(self.function_counter)
        self.function_counter += 1
        inner_function_name = id_name+"()"
        outer_function_name = "_"+inner_function_name

        inner_function = "function "+inner_function_name+"{\n"+function_code+"\n}\n"

        outer_function = "function "+outer_function_name+"{\n"
        outer_function += "let a = document.getElementById('"+id_name+"');\n"
        outer_function += "a.innerHTML ="+inner_function_name+"\n"
        outer_function += "}\n"

        self.script += inner_function
        self.script += outer_function

        button = "<button onclick="+outer_function_name+">"+text+"</button>"
        div = "<div id='"+id_name+"'></div>"

        self.body += button+div

    def _add_set(self, arguments):
        var_name = arguments.split(" ")[0]
        value = arguments.split(" ")[len(var_name)]
        self.variables[var_name] = value

        self.script += "var "+var_name+"="+value+";\n"

    def _add_video(self, arguments):
        self.body += "<video src='"+arguments+"' controls>"
    
    def get_file(self):
        return self.html_header+self.script+"</script>"+self.body+"</body></html>"
    
    def process_markup(self, markup):
        i = 0
        while i < len(markup):
            character = markup[i]
            if character == "[":
                command = markup[i+1:].split(" ")[0].strip()
                arguments = markup[i+len(command)+1:].split("]")[0].strip()

                if command in self.commands.keys():
                    self.commands[command](arguments)
                else:
                    self.body += "<"+command+">"+arguments+"</"+command+">"
                i += len(markup[i+1:].split(" ")[0])+len(markup[i+len(command)+1:].split("]")[0])+1
            elif character == "\\":
                self.body += "<br>\n"
            else:
                self.body += character
            i += 1


def index_file(files):
    html = "<!DOCTYPE html>\n"\
           "<html>\n"\
           "<head>\n"\
           "<meta http-equiv='Content-Type' content='text/html' charset='utf-8'>\n"\
           "</head>"\
           "<body>\n"
    for file in files:
        html += "<a href='"+file+"'>"+file+"</a><br>\n"
    html += "</body>\n</html>"
    return html


class PMarkup:
    def __init__(self, input_folder, output_folder):
        copy_tree(input_folder, output_folder)
        markup_filepaths = glob.glob(output_folder+"**/*.txt", recursive=True)

        for markup_filepath in markup_filepaths:
            with open(markup_filepath, "r", encoding="utf-8") as f:
                markup = f.read()
            instance = MarkupFile()
            instance.process_markup(markup)
            html_filepath = markup_filepath.replace("txt", "html")
            with open(html_filepath, "w", encoding="utf-8") as f:
                f.write(instance.get_file())

        index_paths = [i.replace("txt","html").replace("\\","/").replace(output_folder,".") for i in markup_filepaths]
        print(index_paths)
        with open(output_folder+"/index.html", "w", encoding="utf-8") as f:
            f.write(index_file(index_paths))
