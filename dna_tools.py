import sublime
import sublime_plugin

# IUPAC DNA complement map (case-preserving)
DNA_COMPLEMENT = str.maketrans(
    "ACGTRYKMSWBDHVNacgtrykmswbdhvn",
    "TGCAYRMKSWVHDBNtgcayrmkswvhdbn"
)

class ReverseComplementCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                original = self.view.substr(region)
                revcomp = original[::-1].translate(DNA_COMPLEMENT)
                self.view.replace(edit, region, revcomp)

class ComplementOnlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                original = self.view.substr(region)
                comp = original.translate(DNA_COMPLEMENT)
                self.view.replace(edit, region, comp)

class ReverseOnlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                original = self.view.substr(region)
                rev = original[::-1]
                self.view.replace(edit, region, rev)
