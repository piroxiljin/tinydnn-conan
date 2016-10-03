from conans import ConanFile, CMake, tools
import sys, os

class SQLiteCppConan(ConanFile):
    name = "tiny-dnn"
    version = "1.0.0a"
    url = "https://github.com/sunsided/tinydnn-conan"
    license = "BSD"
    exports = "Findtiny-dnn.cmake"

    def source(self):
        #extension = "zip" if sys.platform == "win32" else "tar.gz" % self.FOLDER_NAME
        #base_name = "%s" % (self.version)
        #zip_name = "%s.%s" % (base_name, extension)
        #url = "https://github.com/tiny-dnn/tiny-dnn/archive/v%s" % (zip_name)
        #self.output.info("Downloading %s..." % url)
        #tools.download(url, zip_name)
        #tools.unzip(zip_name, ".")
        #os.unlink(zip_name)
        #os.rename("tiny-dnn-%s" % base_name, "tiny-dnn")
        commit = "980f9e5fa8e9a4b022e867f2bb86429dd56e555c"
        zip_name = "%s.zip" % commit
        url = "https://github.com/tiny-dnn/tiny-dnn/archive/%s" % (zip_name)
        self.output.info("Downloading %s..." % url)
        tools.download(url, zip_name)
        tools.unzip(zip_name, ".")
        os.unlink(zip_name)
        os.rename("tiny-dnn-%s" % commit, "tiny-dnn")

    def build(self):
        pass

    def package(self):
        self.copy("Findtiny-dnn.cmake", ".", ".")
        self.copy("*.h",   dst="include/tiny_dnn", src="tiny-dnn/tiny_dnn", keep_path=True)
        self.copy("*.hpp", dst="include/tiny_dnn", src="tiny-dnn/tiny_dnn", keep_path=True)
        self.copy("*.h",   dst="include/cereal", src="tiny-dnn/cereal", keep_path=True)
        self.copy("*.hpp", dst="include/cereal", src="tiny-dnn/cereal", keep_path=True)

    def package_info(self):
        pass
