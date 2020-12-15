# Django Signals to Simplify and Decouple Code

### When to Use Signals

It is not meant to be used at every turn. There are particular scenarios where it is highly recommended that we use Django signals, and they include:

- When we have many separate pieces of code interested in the same events, a signal would help distribute the event notification as opposed to us invoking all of the different pieces of code at the same point, which can get untidy and introduce bugs
- We can also use Django signals to handle interactions between components in a decoupled system as an alternative to interaction through RESTful communication mechanisms
- Signals are also useful when extending third-party libraries where we want to avoid modifying them, but need to add extra functionality

> Options

-    pre_init
-    post_init
-    pre_save
-    post_save
-    pre_delete
-    post_delete
-    m2m_changed
-    class_prepared


