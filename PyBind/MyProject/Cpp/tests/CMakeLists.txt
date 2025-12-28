include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/release-1.12.1.zip
)
FetchContent_MakeAvailable(googletest)

add_executable(test_core test_core.cpp)
target_link_libraries(test_core PRIVATE myproject_cpp gtest_main)

add_test(NAME test_core COMMAND test_core)
