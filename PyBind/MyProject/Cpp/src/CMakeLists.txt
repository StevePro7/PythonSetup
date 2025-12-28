add_library(myproject_cpp SHARED core.cpp)

target_include_directories(myproject_cpp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

set_target_properties(myproject_cpp PROPERTIES POSITION_INDEPENDENT_CODE ON)
