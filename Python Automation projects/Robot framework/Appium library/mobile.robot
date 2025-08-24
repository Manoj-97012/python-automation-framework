*** Settings ***
Library    AppiumLibrary

*** Variables ***
${REMOTE_URL}    http://localhost:4723
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    15
${DEVICE_NAME}    10BD9S3A1Y0005N
${APP_PACKAGE}    com.google.earth
${APP_ACTIVITY}   com.google.android.apps.earth.flutter.EarthFlutterActivity

*** Test Cases ***
Open App And Click Button
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    platformVersion=${PLATFORM_VERSION}
    ...    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}    automationName=UiAutomator2
