#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostComputeConan(ConanFile):
    name = "boost_compute"
    version = "1.67.0"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["compute"]
    is_header_only = True

    def package_id_additional(self):
        self.info.header_only()

    requires = (
        "boost_algorithm/1.67.0@bincrafters/testing",
        "boost_array/1.67.0@bincrafters/testing",
        "boost_assert/1.67.0@bincrafters/testing",
        "boost_chrono/1.67.0@bincrafters/testing",
        "boost_config/1.67.0@bincrafters/testing",
        "boost_core/1.67.0@bincrafters/testing",
        "boost_filesystem/1.67.0@bincrafters/testing",
        "boost_function/1.67.0@bincrafters/testing",
        "boost_function_types/1.67.0@bincrafters/testing",
        "boost_fusion/1.67.0@bincrafters/testing",
        "boost_iterator/1.67.0@bincrafters/testing",
        "boost_lexical_cast/1.67.0@bincrafters/testing",
        "boost_mpl/1.67.0@bincrafters/testing",
        "boost_optional/1.67.0@bincrafters/testing",
        "boost_package_tools/1.67.0@bincrafters/testing",
        "boost_preprocessor/1.67.0@bincrafters/testing",
        "boost_property_tree/1.67.0@bincrafters/testing",
        "boost_proto/1.67.0@bincrafters/testing",
        "boost_range/1.67.0@bincrafters/testing",
        "boost_smart_ptr/1.67.0@bincrafters/testing",
        "boost_static_assert/1.67.0@bincrafters/testing",
        "boost_thread/1.67.0@bincrafters/testing",
        "boost_throw_exception/1.67.0@bincrafters/testing",
        "boost_tuple/1.67.0@bincrafters/testing",
        "boost_type_traits/1.67.0@bincrafters/testing",
        "boost_typeof/1.67.0@bincrafters/testing",
        "boost_utility/1.67.0@bincrafters/testing",
        "boost_uuid/1.67.0@bincrafters/testing"
    )

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost_compute"
    description = "Please visit http://www.boost.org/doc/libs/1_67_0"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.67.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()

    # END
