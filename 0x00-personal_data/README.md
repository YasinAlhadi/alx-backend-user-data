# 0x00. Personal data

0. <p>Write a function called <code>filter_datum</code> that returns the log message obfuscated: </p>
<ul>
<li>Arguments:

<ul>
<li><code>fields</code>: a list of strings representing all fields to obfuscate</li>
<li><code>redaction</code>: a string representing by what the field will be obfuscated</li>
<li><code>message</code>: a string representing the log line</li>
<li><code>separator</code>: a string representing by which character is separating all fields in the log line (<code>message</code>)</li>
</ul></li>
<li>The function should use a regex to replace occurrences of certain field values.</li>
<li><code>filter_datum</code> should be less than 5 lines long and use <code>re.sub</code> to perform the substitution with a single regex.</li>
</ul>

1. Log formatter
