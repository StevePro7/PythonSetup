include(FetchContent)

# GoogleTest via FetchContent
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/refs/heads/main.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# Your test binary
add_executable(tests test_core.cpp)

# IMPORTANT: link core *before* gtest
target_link_libraries(tests PRIVATE
        core           # ← this pulls in the include directory
        gtest
        gtest_main
        )

include(GoogleTest)
gtest_discover_tests(tests)
