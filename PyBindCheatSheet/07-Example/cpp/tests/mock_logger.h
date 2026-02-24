#ifndef _MOCK_LOGGER_H_
#define _MOCK_LOGGER_H_

#include <gmock/gmock.h>
#include "../src/core/mesh_processor.h"

class MockLogger : public core::ILogger 
{
public:
	MOCK_METHOD(void, log, (const std::string&), (override));
};

#endif// _MOCK_LOGGER_H