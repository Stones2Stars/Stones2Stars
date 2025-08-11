#pragma once

#ifndef Win32_h__
#define Win32_h__

#include "CvGameCoreDLL.h"

struct Win32
{
	static void update_hooks();

	static void pythonPublish();

	static bool isFocused();
	static HWND getToplevelWindow();
	static POINT getCursorPos();
	static bool isLMB();
	static bool isRMB();
	static bool isMMB();
	static POINT screenToClient(POINT screenPos);

	static int registerMouseWheelListener();
	static void unregisterMouseWheelListener(int handle);
	static float getMouseWheelDiff(int handle);
};

#endif // Win32_h__
