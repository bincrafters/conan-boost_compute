from conans import ConanFile, tools


class BoostComputeConan(ConanFile):
    name = "Boost.Compute"
    version = "1.65.1"
    requires = \
        "Boost.Algorithm/1.65.1@bincrafters/testing", \
        "Boost.Array/1.65.1@bincrafters/testing", \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Chrono/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Filesystem/1.65.1@bincrafters/testing", \
        "Boost.Function/1.65.1@bincrafters/testing", \
        "Boost.Function_Types/1.65.1@bincrafters/testing", \
        "Boost.Fusion/1.65.1@bincrafters/testing", \
        "Boost.Iterator/1.65.1@bincrafters/testing", \
        "Boost.Lexical_Cast/1.65.1@bincrafters/testing", \
        "Boost.Mpl/1.65.1@bincrafters/testing", \
        "Boost.Optional/1.65.1@bincrafters/testing", \
        "Boost.Preprocessor/1.65.1@bincrafters/testing", \
        "Boost.Property_Tree/1.65.1@bincrafters/testing", \
        "Boost.Proto/1.65.1@bincrafters/testing", \
        "Boost.Range/1.65.1@bincrafters/testing", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing", \
        "Boost.Thread/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Tuple/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing", \
        "Boost.Typeof/1.65.1@bincrafters/testing", \
        "Boost.Utility/1.65.1@bincrafters/testing", \
        "Boost.Uuid/1.65.1@bincrafters/testing"
    lib_short_names = ["compute"]
    is_header_only = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-compute"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    def package_id(self):
        if self.is_header_only:
            self.info.header_only()

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
