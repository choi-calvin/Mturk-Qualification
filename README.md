# Publishing MTurk Qualification with Boto 3
Demonstration of creating and posting a Qualification HIT for Amazon MTurk in Boto 3.
The default questions and answers were designed for use in [Duncan Lab](https://www.duncanlab.org), however, they may be configured for alternative use.
Proper documentation may be consulted for more help [here](http://boto3.readthedocs.io/en/latest/reference/services/mturk.html).

## Table of Contents
* [Getting Started](#getting-started)
    * [Installing Prerequisites](#installing-prerequisites)
    * [Configuring the Answer Key](#configuring-the-answer-key)
    * [Publishing the Qualification](#publishing-the-qualification)
        * [Running the Script](#running-the-script)
* [Advanced Options](#advanced-options)
    * [Creating a Question](#creating-a-question)
        * [Creating an Answer Option](#creating-an-answer-option)
    * [Removing a Question](#removing-a-question)
        * [Removing an Answer Option](#removing-an-answer-option)
* [Author(s)](#authors)
* [Acknowledgement(s)](#acknowledgements)

## Getting Started
These instructions are mainly written for research assistants in Duncan Lab and assume a limited understanding of programming of any sort.
### Installing Prerequisites
Amazon's "Boto 3" is normally installed with pip, which comes shipped with Python 3.
To install, open up **Terminal** (on Mac) or **Command Prompt** (on Windows).

Type in the line:
```
pip install boto3
```
Press **Enter** and wait for the installation to finish.
More information can be found in the Boto 3 [Quickstart Guide](https://boto3.readthedocs.io/en/latest/guide/quickstart.html).

### Configuring the Answer Key
In order to modify the answer key for your purposes, open **demo_ans.xml** in an editor of your choice.
Each question in the answer key is written within
```xml
<Question>
</Question>
```
blocks. Each question is distinguished by its unique **QuestionIdentifier**.
Find the question block of which answer choices you want to configure.

Each answer option is written in
```xml
<AnswerOption>
</AnswerOption>
```
blocks, with its unique **SelectionIdentifier**. Find the selection you want to modify.

Within the
```xml
<AnswerScore>x</AnswerScore>
```
block, replace **x** with a numeric value. The number should be either 0 or 1.
To change the option to an accepted answer, change the value to 1. If not, change it to 0.

For example, to make the qualification test to accept only males, the answer key should look like this:
```xml
<Question>
    <QuestionIdentifier>gender</QuestionIdentifier>
    <AnswerOption>
        <SelectionIdentifier>male</SelectionIdentifier>
        <AnswerScore>1</AnswerScore>
    </AnswerOption>
    <AnswerOption>
        <SelectionIdentifier>female</SelectionIdentifier>
        <AnswerScore>0</AnswerScore>
    </AnswerOption>
    <AnswerOption>
        <SelectionIdentifier>other</SelectionIdentifier>
        <AnswerScore>0</AnswerScore>
    </AnswerOption>
</Question>
```
To accept both males and females:
```xml
<Question>
    <QuestionIdentifier>gender</QuestionIdentifier>
    <AnswerOption>
        <SelectionIdentifier>male</SelectionIdentifier>
        <AnswerScore>1</AnswerScore>
    </AnswerOption>
    <AnswerOption>
        <SelectionIdentifier>female</SelectionIdentifier>
        <AnswerScore>1</AnswerScore>
    </AnswerOption>
    <AnswerOption>
        <SelectionIdentifier>other</SelectionIdentifier>
        <AnswerScore>0</AnswerScore>
    </AnswerOption>
</Question>
```
It is allowed to have more than one acceptable answer option.
Having no acceptable answer option is also allowed, however, this will result in the qualification being impossible to attain.

### Publishing the Qualification
After all configurations have been made to the question and answer forms, open **demo_qua.py**.
Additional configurations are required by changing variable values.
These variables are as such:

Variable | Type | Description
--- | --- | ---
AWS_ACCESS_KEY | String | The access key for your AWS account.*
AWS_SECRET_KEY | String | The secret key for your AWS account.*
IS_SANDBOX | Bool | Whether to publish the Qualification to the developer sandbox. A value of **True** publishes to the sandbox.
NAME | String | The name of the Qualification. You cannot have two Qualifications with the same name.
DESCRIPTION | String | A brief description of the Qualification, capped at 2000 characters.
KEYWORDS | String | Keywords that help workers search for the Qualification. Each keyword must be separated by a comma, no spaces. Capped at 1000 characters.
TEST_DURATION_IN_SECONDS | Int | The maximum time the worker has to complete the Qualification.

<sup>*These have a high level of security. It is recommended that they be saved in a safe location and not in the script itself.</sup>

#### Running the Script
After all the variables have been assigned the appropriate values, the script must be run.
This can be done from within a Python IDE of your choice.
If not, you can run the script from the terminal like so:

1. Open up **Terminal** on Mac, or **Command Prompt** on Windows.
2. Type in "python " without the quotations marks. Note the space at the end.
3. Type in the path of **demo_qua.py**. A short way to do this is to drag and drop the file into **Terminal/Command Prompt**.
4. Press "Enter" to run the script. If no errors have occurred, the Qualification is now published!

## Advanced Options
### Creating a Question
Unfortunately, the only type of questions accepted for automated marking is multiple choice.
First, open **demo_qs.xml** in the editor of your choice.
Similar to the answer key, each question is written within
```xml
<Question>
</Question>
```
blocks, with its corresponding **QuestionIdentifier**.

Anywhere in the space between questions, add the following code:
```xml
<Question>
    <QuestionIdentifier>example_identifier</QuestionIdentifier>
    <DisplayName>Example Display Name</DisplayName>
    <IsRequired>true</IsRequired>
    <QuestionContent>
        <Text>Example Text</Text>
    </QuestionContent>
    <AnswerSpecification>
        <SelectionAnswer>
            <Selections>

            </Selections>
        </SelectionAnswer>
    </AnswerSpecification>
</Question>
```
The **QuestionIdentifier** can be any string, provided it is not used by any other question.
It is recommended to use a smart identifier that relates to the question.
This value will be used later on in the answer key.
Replace **example_identifier** in the code above with your identifier.

Give the question a unique **DisplayName** as well.
Replace **Example Display Name** in the code above.

Replace **Example Text** with your question text.
This is what will be shown to the worker completing the qualification test.
For example:
```xml
<Text>Do you have any previous experience with psychological experiments?</Text>
```
Next, open **demo_ans.xml** in the editor of your choice.
The layout is similar as in the question key.
In between any question block, add the following code:
```xml
<Question>
    <QuestionIdentifier>example_identifier</QuestionIdentifier>

</Question>
```
Replace **example_identifier** with the same **QuestionIdentifier** that you chose in the question key.

Next, scroll to the bottom of the answer key and find the following block of code:
```xml
<QualificationValueMapping>
    <PercentageMapping>
        <MaximumSummedScore>x</MaximumSummedScore>
    </PercentageMapping>
</QualificationValueMapping>
```
Here, **x** should always correspond to the number of questions in the qualification test.
Since you have added a new question, increase the current value of **x** by 1.
**Failure to follow this instruction will result in the invalid marking of tests.
This step is very important.**

#### Creating an Answer Option
In **demo_qs.xml**, add the following code between **\<Selections>** and **\</Selections>**
```xml
<Selection>
    <SelectionIdentifier>example_identifier</SelectionIdentifier>
    <Text>Example Text</Text>
</Selection>
```
This will add a new answer option to the question.

Replace **example_identifier** with a unique identifier relating to the answer option.

Replace **Example Text** as well. This will be the text that is shown to the worker completing the qualification test.

Next, open **demo_ans.xml** and locate the question that you added the answer option to.
Within **\<Question>** and **\</Question>** add the following:
```xml
<AnswerOption>
    <SelectionIdentifier>example_identifier</SelectionIdentifier>
    <AnswerScore>x</AnswerScore>
</AnswerOption>
```
Replace **example_identifier** with the same unique identifier used in **demo_qs.xml**.

Replace **x** with your score.
This value should be either 0 or 1, depending on whether this answer option is accepted or not.
For more information, see [**Configuring the Answer Key**](#configuring-the-answer-key).

### Removing a Question
First, open **demo_qs.xml** and locate the question you wish to remove (by its **QuestionIdentifier**).
The entire question should be within opening and closing **Question** tags, like so:
```xml
<Question>
    *** Question Content ***
</Question>
```
Select and delete the entire block (including the opening and closing tags).

Next, open **demo_ans.xml** and locate the corresponding question block (with the same **QuestionIdentifier**).
Select and delete it, as in the question key.

Finally, scroll down to the following code:
```xml
<QualificationValueMapping>
    <PercentageMapping>
        <MaximumSummedScore>x</MaximumSummedScore>
    </PercentageMapping>
</QualificationValueMapping>
```
The value **x** should always correspond to the number of questions in the qualification test.
Since you have removed a question, decrease the value of **x** by 1.

#### Removing an Answer Option
Open **demo_qs.xml** and locate the question you wish to remove the answer option from.
Locate the answer option. It should look like so:
```xml
<Selection>
    <SelectionIdentifier>example_identifier</SelectionIdentifier>
    <Text>Example Text</Text>
</Selection>
```
Select and delete this entire block of code.

Then, open **demo_ans.xml** and locate the corresponding answer option.
It should look like so:
```xml
<AnswerOption>
    <SelectionIdentifier>example_identifier</SelectionIdentifier>
    <AnswerScore>x</AnswerScore>
</AnswerOption>
```
Make sure the **SelectionIdentifier** is the same as in the question key.
Select and delete this entire block of code.

**Note:** After removing an answer option, make sure that at least one answer option in that question has an **AnswerScore** of 1.
If not, the qualification will be impossible to attain.
More information on how to change this value can be found in [Configuring the Answer Key](#configuring-the-answer-key).

## Author(s)
* **Calvin Choi**

## Acknowledgement(s)
* **Katherine Wood**
    * Code from [this](https://katherinemwood.github.io/post/qualifications/) kind post was modified for personal use