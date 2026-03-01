# ---- GoogleTest ----
include(FetchContent)
FetchContent_Declare(
        googletest
        GIT_REPOSITORY https://github.com/google/googletest.git
        GIT_TAG v1.14.0
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# ---- Test executable ----
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
