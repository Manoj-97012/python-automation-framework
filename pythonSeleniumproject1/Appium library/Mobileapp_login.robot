*** Settings ***
Library    AppiumLibrary

*** Variables ***
${REMOTE_URL}    http://localhost:4723
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    15
${DEVICE_NAME}    10BD9S3A1Y0005N
${APP_PACKAGE}      com.cashkaro
${APP_ACTIVITY}     com.cashkaro.MainActivity

*** Test Cases ***
Full Cashback Flow For Amazon
    [Documentation]    Launch app → Sign in → Search Amazon → Visit → Confirm browser opened
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}    automationName=UiAutomator2

    Wait Until Page Contains Element    xpath=//android.widget.TextView[@text='Next']
    Click Element    xpath=//android.widget.TextView[@text='Next']
    Click Element    xpath=//android.widget.TextView[@text='Next']
    Click Element    xpath=//android.widget.TextView[@text='Get Started']
    Wait Until Page Contains Element    xpath=//android.widget.TextView[@text='CONTINUE']
    CLICK ELEMENT    xpath=//android.widget.TextView[@text='CONTINUE']
    wait until page contains element    xpath=//android.widget.TextView[@text='Allow']
#    wait until page contains element    xpath=//android:id/button2
#    CLICK BUTTON    xpath=//android:id/button2
    CLICK ELEMENT   xpath=//android.widget.TextView[@text='Allow']
    #Input Text       xpath=(//android.view.ViewGroup)[3]//android.widget.EditText    Hello World
    WAIT UNTIL PAGE CONTAINS ELEMENT    xpath=//*[@resource-id='com.android.permissioncontroller:id/permission_allow_button']
    Click Element    xpath=//*[@resource-id='com.android.permissioncontroller:id/permission_allow_button']
    CLICK ELEMENT    xpath=//com.horcrux.svg.C
    wait until page contains element    xpath=//android.widget.TextView[@text='Mobiles']
    CLICK ELEMENT   xpath=//android.widget.TextView[@text='Mobiles']
    wait until page contains element    xpath=//*[contains(@text,'₹61,390')]
    ${amount_1}=    Get Text    xpath=//*[contains(@text,'₹61,390')]
    wait until page contains element    xpath=//android.widget.TextView[@text='Apple iPhone 15 (Black, 128GB Storage)']
    CLICK ELEMENT   xpath=//android.widget.TextView[@text='Apple iPhone 15 (Black, 128GB Storage)']
    Wait Until Element Is Visible    xpath=//android.widget.TextView[contains(@text,'View Breakdown')]    15s
    Click Element                    xpath=//android.widget.TextView[contains(@text,'View Breakdown')]
    ${amount_2}=    Get Text    xpath=//*[contains(@text,'₹61,390')]
    Should Contain    ${amount_1}    ${amount_2}