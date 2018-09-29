#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostComputeConan(base.BoostBaseConan):
    name = "boost_compute"
    url = "https://github.com/bincrafters/conan-boost_compute"
    lib_short_names = ["compute"]
    header_only_libs = ["compute"]
    b2_requires = [
        "boost_algorithm",
        "boost_array",
        "boost_assert",
        "boost_chrono",
        "boost_config",
        "boost_core",
        "boost_filesystem",
        "boost_function",
        "boost_function_types",
        "boost_fusion",
        "boost_iterator",
        "boost_lexical_cast",
        "boost_mpl",
        "boost_optional",
        "boost_preprocessor",
        "boost_property_tree",
        "boost_proto",
        "boost_range",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_thread",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits",
        "boost_typeof",
        "boost_utility",
        "boost_uuid"
    ]


