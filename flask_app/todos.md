# TODOS

Dashboard

Projects
    - Project should be individually selectable
        - Selecting project should set project in session
        - Schedules / Tests / Reports should only show according to project selected

Schedule
    - "Delete Schedule" functionality
    - Individual Schedule Page
        - Check boxes to verify receipt of field report
        - Update field sheet should be done within the schedule
            - Field sheet form should include selector for test type.
                - Types including Concrete, Soil, Inspection, Other
        - Soil Sample Pickup and Concrete Sampling should have "Assign Testing" link
Earthwork
    - Assign tests to individual schedules/work orders
        - Field tests also assigned here.
        - Example Id: [projectnumber]001-F1 for field test or [projectnumber]001-L1 for laboratory sample
    - Add basic testing suite (Proctor, Sieve Analysis, Organic Content, Atterberg Limits, Field Density)
        - Create data entry sheets
        - Create display for results
        - Generate Reports
            - Generic Proctor Report, Individual test reports, Density Report
Concrete
    - Assign Tests to Concrete Sampling
        - User will enter number of samples taken for particular schedule
        - Page will render the tests and checkboxes for each sample
        - Page will generate sample ID in this format: [SCHEDULE-ID]-C01, -C02, -C03, etc...
    - Concrete Samples List
        - Once tests are assigned, samples will show up in the concrete samples log
    - Add Test Results
        - Wil be accessed via sample log
Inspections

Reports

Equipment

## CODE CLEANUP

    - Delete functions are all "delete_recipe()"