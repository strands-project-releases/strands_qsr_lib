^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package qsr_lib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.1.1 (2015-06-19)
------------------
* Adding test depends
* Fixing qtcbc collapse bug
* Adding qtcbc and currently used string representation test.
* Adding unit tests for qtcb and qtcc
* Contributors: Christian Dondrup

0.1.0 (2015-06-16)
------------------
* fix mos in example
* Getting rid of parameters namespace inside of dynamic_args.
* Merge branch 'master' into qtc_params
  Conflicts:
  qsr_lib/scripts/example_ros_client.py
* Moved qtc parameters to service call
  Using dynamic_args and the newly created field 'parameters'.
  Should be fully backwards compatible with the option of removing this later on.
* Example client bug fix
  The mos test broke all the other QSR which don't define `q`.
  Commented it and using the more generic service call now.
* qsr MOS (moving or stationary)
* Merge pull request `#59 <https://github.com/strands-project/strands_qsr_lib/issues/59>`_ from yianni/58
  cone_direction now complies with --future (closes `#58 <https://github.com/strands-project/strands_qsr_lib/issues/58>`_)
* Merge pull request `#60 <https://github.com/strands-project/strands_qsr_lib/issues/60>`_ from yianni/qtc-future
  qtc compliant with future, closes `#50 <https://github.com/strands-project/strands_qsr_lib/issues/50>`_
* Merge pull request `#56 <https://github.com/strands-project/strands_qsr_lib/issues/56>`_ from yianni/change-ini
  changed config files from ini format to yaml
* qtc compliant with future, closes `#50 <https://github.com/strands-project/strands_qsr_lib/issues/50>`_
* --amend
* updated shortcut for coneDir
* cone_direction now complies with --future (closes `#58 <https://github.com/strands-project/strands_qsr_lib/issues/58>`_)
* shortened return string
* providing example of config format for arg_relations_distance
* changed config files from ini format to yaml
* add_object_track_from_list propagates **kwargs to Object_State
* added funtionality to add an object's track from a list of values
* Contributors: Christian Dondrup, Peter Lightbody, Yiannis Gatsoulis

0.0.8 (2015-05-17)
------------------
* args_distance no longer read default ini and being init to an empty dict
* more informative error message
* Changed args_distance to use dynamic_args
  - deprecating relations_and_values, for now still works and gives warning
  - changed defaults of args_distance to start uninitialized
* simplified dc computation
* Merge branch 'master' into rcc2
* added abstract method custom_set_ini to cone qsr
* Merge branch 'master' of github.com:strands-project/strands_qsr_lib into 49
* Copy and paste qsrs_for logic from base abstract class and painfully finding out that two leading underscores means really private.
* Merge branch 'master' into qsrs_for
  Conflicts:
  qsr_lib/src/qsrlib_qsrs/qsr_qtc_simplified_abstractclass.py
* Merge pull request `#37 <https://github.com/strands-project/strands_qsr_lib/issues/37>`_ from cdondrup/strings
  QTC now returns real qtc symbol strings: +,-,0
* added RCC2
* removed dbg print statement
* added support for reading from ini file at start and at runtime
  - also fixed a bug in
  qsr_arg_relations_abstractclass/__check_validity_of_qsr_relations_and_values
* added support to represent qsr fields as dictionaries
* changed reference object
* dbg cone directions
* cone_direction QSR added
* Amended Comments
* added some test/debug tools for regional QSRs
* Added RCC8 to qsr_lib
* fixed bug
* removed misleading comments
* removed misleading comments
* fixed incorrect computation of symmetrical RCC3 relations, closes `#40 <https://github.com/strands-project/strands_qsr_lib/issues/40>`_
* Checking if boolean values are really boolean.
* Calculating qtc relations between all given objects and using qsrs_for
* Using new string results for all possible combinations function as well.
* QTC now returns real qtc symbol strings: +,-,0
* Contributors: Christian Dondrup, Peter Lightbody, Yiannis Gatsoulis

0.0.7 (2015-04-22)
------------------
* changed in qsrs/arg_distance the qsrs_for_default to not include mirrors and be alphabetically sorted
* changed to sorter code rcc3 custom checks for qsrs_for (same to arg_distance corrected one)
* fixed qsrs_for bug that did not perform correctly custom check in qsr_arg_relations_distance
* arg_relations_distance QSR
* added doc to qsr_abstraclass.custom_checks_for_qsrs_for, added rcc3.custom_checks_for_qsrs_for, closes `#32 <https://github.com/strands-project/strands_qsr_lib/issues/32>`_ which was OK
* closes `#30 <https://github.com/strands-project/strands_qsr_lib/issues/30>`_ and `#26 <https://github.com/strands-project/strands_qsr_lib/issues/26>`_
* Contributors: Yiannis Gatsoulis

0.0.6 (2015-03-04)
------------------
* Closes `#23 <https://github.com/strands-project/strands_qsr_lib/issues/23>`_: removed annoying message: "Resetting QSRlib data"
* Removing the `end` operator
* Using rospy.log* for ROS node outputs. Prevents spamming the terminal bu setting most of it to debug level
* Contributors: Christian Dondrup, Yiannis

0.0.5 (2015-02-27)
------------------
* There was a tag with a higher version number. Adjusting numbers to release for necessary bug fixes in the ROS client.
* Contributors: Christian Dondrup

0.0.3 (2015-01-27)
------------------

0.0.2 (2015-01-27)
------------------

0.0.1 (2015-01-27)
------------------
* Adding proper install targets and adjusting package.xml
* Update README.md
* Added .md to readme to make it markdown
* Fixing spelling mistake and adding QTC description to README
* Removing some prints and explicitly setting quantisation_factor to 0 if None in the make function.
* Adding custom test to see if x and y are defined.
* Adding an optional argument to omit collapsing qtc states.
  Adding ability to read a csv file with xy coordinates for the qtc representation
* Adding collapse functionality to collapse similar adjacent states
* nan value for empty fields in world_trace/Object_State
* Added the option of reading the incoming object data from a file using the example ros client to make it easier to test QSRs
  Does not change the the default behaviour.
  Also added a few optional arguments just for qtc.
* Added correct validation function
* Added:
  * validation argument
  * quantisation_factor argument
  * custom help
  * custom check
  Bugs: Validation is not working correctly yet. Only accounts fro transitions from -1 to 1 and vice-versa. Many more constraints to be added.
* Added quantisation factor
* Added new line at end of file
* * Adding QTCC
  * the abstract class now contains all the relevant code. The implementing classes only select the part of the QTCC tuple they want to return and implement the custom_* functions
* Added parent class to compute qtc states from incoming position arrays.
  Computes qtcc, for qtcb the last two values can simply be omitted.
  Issues:
  * Has only been tested for the distance constraint so far
  * Needs validation of state chains, this includes the insertion of virtual timestamps
  * So far there is no need for it to be abstract, might be changed in future
  * Quantisation factor has to be given together with the data
* QSRlib, uses new IO, major change
* removed timestamps list
* removed legacy files
* check in
* python new qsrlib ready
* check in
* legacy tidy up
* check in
* check in
* breaking
* moving
* check in
* qtc_b in progress -bugged euclidean
* added support for reusing previous passed input_data (if wanted)
* Various and very importants (see comments below for details)
  1) Renamed class QSR_Lib to QSRlib
  2) Renamed request methods in QSRlib and in the QSRlib_ROS_Server
  to have the same name "request_qsrs"
  3) Renamed qsr_lib_ros_* to qsrlib_ros_*
  4) Provided an example of using the QSRlib_ROS_Client for ease of
  read
  5) README updated to reflect the changes
* fixed a bug on example.py
* qsrlib instracture + example RCC3 2D rectangles for devs
* Contributors: Christian Dondrup, Yiannis Gatsoulis
