*** Settings ***
Library    AppiumLibrary

*** Variables ***
${REMOTE_URL}    http://localhost:4723
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    15
${DEVICE_NAME}    10BD9S3A1Y0005N
${APP_PACKAGE}    com.google.android.gm
${APP_ACTIVITY}   com.google.android.gm.ConversationListActivityGmail

*** Test Cases ***
Login the app in mobile
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM_NAME}    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}    automationName=UiAutomator2

    click element    id=com.google.android.gm:id/welcome_tour_got_it
    wait until element is visible    com.google.android.gm:id/action_done
    click element    com.google.android.gm:id/action_done



