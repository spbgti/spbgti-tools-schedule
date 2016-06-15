Schedule service API
====================


.. code-block:: python
   :linenos:
   """
    returns all groups that have any schedules. Old schedules supposed to be deleted;
   """

   def get_all_groups():



.. code-block:: python
   :linenos:

   get_schedule_by_group(group_id)

returns full schedule for the selected group;

.. code-block:: python
   :linenos:

   get_schedule_by_group_and_day(group_id, day)

returns one day schedule for specific group;

.. code-block:: python
   :linenos:

   get_schedule_by_teacher(teacher_id)

returns the teacher’s schedule. This will help students to find teacher, when he is needed;

.. code-block:: python
   :linenos:

   get_schedule_by_location_room(room_id)

returns schedule for a particular room. This will help students check if a room is empty in a specific time;

.. code-block:: python
   :linenos:

   get_empty_rooms_by_location_and_time(location_id, time_range)

returns empty rooms that could be used on a specific location in a selected time range. This will help student find a room for example on a specific department where he/she can freely study not disturbing anyone;

.. code-block:: python
   :linenos:

   get_schedule_by_group_nearest(group_id)

returns information about the nearest class for a specified group. This could be used in case you need to find the next pair, which you should visit.
