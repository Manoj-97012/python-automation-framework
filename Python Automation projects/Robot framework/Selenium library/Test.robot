*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To Login Page
Suite Teardown    Close Browser

*** Variables ***
${URL}      https://testautomationpractice.blogspot.com/
${BROWSER}  chrome
${Point_me}     //button[text()='Point Me']

*** Test Cases ***
Verify the All Inputs in website
    Input Text    id:name    Manoj
    input text    id:email   akulamanoj
    input text    xpath://input[@id='phone']    9701240422
    PAGE SHOULD CONTAIN    Automation Testing Practice

Verify the radio buttons
    ${radio}=   click element    xpath://input[@id='male']
    log to console    ${radio}

Verify the checkbox in webpage
    click element    id:sunday
    checkbox should be selected     id:sunday

Verify the dropdown in webpage
    Select From List By Label    id=country    India
    ${selected}=    Get Selected List Label    id=country
    Should Be Equal    ${selected}    India

Verify the colour in webpage
    ${colours}=     get list items    xpath://select[@id='colors']
    log to console    ${colours}

Verify the drop click element
    input text    xpath://input[@id='field1']       Hello world
    click button    xpath://button[normalize-space()='Copy Text']
Verify the static web element
    ${text}=    click element    xpath://*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th[1]
    log to console    ${text}

Verify the broken link
    ${link}=    click link    xpath://a[normalize-space()='Errorcode 400']
    page should contain    Bad Request
    go back

Verify the mouse cover
    sleep    10s
    mouse over    ${Point_me}


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
