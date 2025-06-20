*** Settings ***
Library    AppiumLibrary

*** Variables ***
${REMOTE_URL}    http://localhost:4723
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    15
${DEVICE_NAME}    10BD9S3A1Y0005N
${APP_PACKAGE}      com.swaglabsmobileapp
${APP_ACTIVITY}     com.swaglabsmobileapp.MainActivity

*** Test Cases ***
Login the app in mobile
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}    automationName=UiAutomator2

    Input Text    xpath=(//android.widget.EditText)[1]   standard_user
    Input text    xpath=(//android.widget.EditText)[2]   secret_sauce
    click element    xpath=//android.widget.TextView
    Wait Until Page Contains Element    xpath=//android.widget.TextView[@text='ADD TO CART']
    Click Element    xpath=//android.widget.TextView[@text='ADD TO CART']
    Wait Until Page Contains Element    xpath=//android.widget.ImageView
    Click Element    xpath=//android.widget.ImageView
    Wait Until Page Contains Element    xpath=//android.widget.TextView[@text='CONTINUE SHOPPING']      10 seconds
    Click Element    xpath=//android.widget.TextView[@text='CONTINUE SHOPPING']