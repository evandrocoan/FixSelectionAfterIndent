

import sublime
import sublime_plugin


class IndentSelectWholeFirstLineEventListener(sublime_plugin.EventListener):

    def on_post_text_command(self, view, command_name, args):

        if command_name == 'indent':

            if all(not sel.empty() for sel in view.sel()):

                if all(view.line(sel.begin()) != view.line(sel.end()) for sel in view.sel()):
                    new_selections = []

                    for sel in view.sel():
                        new_selections.append(sel.cover(view.line(sel.begin())))

                    view.sel().clear()
                    view.sel().add_all(new_selections)



