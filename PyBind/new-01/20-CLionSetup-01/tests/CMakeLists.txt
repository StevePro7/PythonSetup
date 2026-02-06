add_executable(my_api_tests
        test_api.cpp
        )

target_link_libraries(my_api_tests
        PRIVATE
        my_api
        GTest::gtest_main
        )

include(GoogleTest)
gtest_discover_tests(my_api_tests)
