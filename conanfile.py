from conans import ConanFile, tools, os

class BoostComputeConan(ConanFile):
    name = "Boost.Compute"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/compute"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "compute"
    requires =  "Boost.Algorithm/1.64.0@bincrafters/testing", \
                      "Boost.Array/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Chrono/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Filesystem/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Function_Types/1.64.0@bincrafters/testing", \
                      "Boost.Fusion/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Property_Tree/1.64.0@bincrafters/testing", \
                      "Boost.Proto/1.64.0@bincrafters/testing", \
                      "Boost.Range/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Thread/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Tuple/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Typeof/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing", \
                      "Boost.Uuid/1.64.0@bincrafters/testing"

                      #algorithm9 array3 assert1 chrono8 config0 core2 filesystem8 function5 function_types5 fusion5 iterator5 lexical_cast8 mpl5 optional5 preprocessor0 property_tree13 proto8 range7 smart_ptr4 static_assert1 thread11 throw_exception2 tuple4 type_traits3 typeof5 utility5 uuid12
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)

    def package_id(self):
        self.info.header_only()