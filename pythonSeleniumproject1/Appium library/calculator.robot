*** Settings ***
Library    AppiumLibrary

*** Variables ***
${REMOTE_URL}    http://localhost:4723
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    15
${DEVICE_NAME}    10BD9S3A1Y0005N
${APP_PACKAGE}    com.vivo.calculator
${APP_ACTIVITY}   com.vivo.calculator.Calculator

*** Test Cases ***
Addition Test On Calculator
    [Documentation]    Test 2 + 3 = 5 in Android calculator app
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}    automationName=UiAutomator2

    Click Element    id=com.vivo.calculator:id/digit_7
    Click Element    id=com.vivo.calculator:id/op_add
    Click Element    id=com.vivo.calculator:id/digit_6
    Click Element    id=com.vivo.calculator:id/eq

    ${result}=    Get Text    id=com.vivo.calculator:id/formula
    Should Be Equal    ${result}    13

    Close Application