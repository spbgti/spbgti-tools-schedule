Schedule service API
====================

Here we listed all the api, that should be implemented for **schedule service**.

.. code-block:: python

   """
    returns all groups that have any schedules.
    Old schedules supposed to be deleted;
   """

   def get_all_groups():

   """
    Returns full schedule for the selected group;
   """

   def get_schedule_by_group(group_id):

   """
    Returns one day schedule for specific group;
   """

   def get_schedule_by_group_and_day(group_id, day):

   """
    Returns the teacher’s schedule.
    This will help students to find teacher, when he is needed;
   """

   def get_schedule_by_teacher(teacher_id):

   """
    Returns schedule for a particular room.
    This will help students check if a room is empty in a specific time;
   """

   def get_schedule_by_location_room(room_id):

   """
   Returns empty rooms that could be used on a specific
   location in a selected time range.

   This will help student find a room for example on
   a specific department where he/she can freely study not disturbing anyone;
   """

   def get_empty_rooms_by_location_and_time(location_id, time_range):

   """
    returns information about the nearest class
    for a specified group.

    This could be used in case you need to find the next pair, \
    which you should visit.
   """

   def get_schedule_by_group_nearest(group_id):
