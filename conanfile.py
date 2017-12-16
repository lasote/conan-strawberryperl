from conans import ConanFile, tools
import os


class StrawberryperlConan(ConanFile):
    name = "strawberryperl"
    version = "5.26.0"
    license = "GNU Public License or the Artistic License."
    url = "https://github.com/lasote/conan-strawberryperl"
    settings = "os", "arch"
    description = "Strawbery Perl for Windows. Useful as build_require"
    short_paths = True

    def configure(self):
        if self.settings.os != "Windows":
            raise Exception("Only windows supported for strawberry perl")

    def build(self):
        installer = {"x86": "strawberry-perl-5.26.0.1-32bit-portable.zip",
                     "x86_64": "strawberry-perl-5.26.0.1-64bit-portable.zip"}[str(self.settings.arch)]
        url = "http://strawberryperl.com/download/5.26.0.1/%s" % installer
        tools.download(url, filename="perl.zip")
        tools.unzip("perl.zip")
        os.unlink("perl.zip")

    def package(self):
        self.copy("*", keep_path=True)
        self.copy("licenses/License.rtf*", dst=".", keep_path=False, ignore_case=True)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "perl", "bin"))
        self.env_info.PATH.append(os.path.join(self.package_folder, "c", "bin"))

