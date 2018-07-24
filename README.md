# Qualification
Demonstration of creating and posting a Qualification HIT for Amazon MTurk in Boto 3.
The default questions and answers were designed for use in [Duncan Lab](https://www.duncanlab.org), however, they may be configured for alternative use.
Proper documentation may be consulted for more help [here](http://boto3.readthedocs.io/en/latest/reference/services/mturk.html).

## Table of Contents
* [Getting Started]()
    * [Installing Prerequisites]()
    * [Configuring the Answer Key]()
    * [Publishing the Qualification]()
* [Advanced Options]()
    * [Creating a Question]()
        * [Creating an Answer Option]()
    * [Removing a Question]()
        * [Removing an Answer Option]()
    * [Embedding Media]()
* [Author(s)]()

## Getting Started
These instructions are mainly written for research assistants in Duncan Lab and assume a limited understanding of programming of any sort.
### Installing Prerequisites
Amazon's "Boto 3" is normally installed with pip, which comes shipped with Python 3.
To install, open up "Terminal" (on Mac) or "Command Prompt" (on Windows).

Type in the line:
```
pip install boto3
```
Press **Enter** and wait for the installation to finish.
More information can be found in the Boto 3 [Quickstart Guide](https://boto3.readthedocs.io/en/latest/guide/quickstart.html).

### Configuring the Answer Key
In order to modify the answer key for your purposes, open **demo_ans.xml** in an editor of your choice.
Each question in the answer key is written within
```
<Question>
</Question>
```
blocks. Each question is distinguished by its unique **QuestionIdentifier**.
Find the question block of which answer choices you want to configure.

Each answer option is written in
```
<AnswerOption>
</AnswerOption>
```
blocks, with its unique **SelectionIdentifier**. Find the selection you want to modify.

Within the
```
<AnswerScore>x</AnswerScore>
```
block, replace **x** with a numeric value. The number should be either 0 or 1.
To change the option to an accepted answer, change the value to 1. If not, change it to 0.

For example, to make the qualification test to accept only males, the answer key should look like this:
```
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
```
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
todo

## Advanced Options
### Creating a Question
Unfortunately, the only type of questions accepted for automated marking is multiple choice.
First, open **demo_qs.xml** in the editor of your choice.
Similar to the answer key, each question is written within
```
<Question>
</Question>
```
blocks, with its corresponding **QuestionIdentifier**.

Anywhere in the space between questions, add the following code:
```
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
```
<Text>Do you have any previous experience with psychological experiments?</Text>
```
Next, open **demo_ans.xml** in the editor of your choice.
The layout is similar as in the question key.
In between any question block, add the following code:
```
<Question>
    <QuestionIdentifier>example_identifier</QuestionIdentifier>

</Question>
```
Replace **example_identifier** with the same **QuestionIdentifier** that you chose in the question key.

Next, scroll to the bottom of the answer key and find the following block of code:
```
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
```
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
```
<AnswerOption>
    <SelectionIdentifier>example_identifier</SelectionIdentifier>
    <AnswerScore>x</AnswerScore>
</AnswerOption>
```
Replace **example_identifier** with the same unique identifier used in **demo_qs.xml**.

Replace **x** with your score.
This value should be either 0 or 1, depending on whether this answer option is accepted or not.
For more information, see [**Configuring the Answer Key**]().

### Removing a Question
todo
#### Removing an Answer Option
todo

### Embedding Media
todo

## Author(s)
* **Calvin Choi**