"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from ynab_api.model_utils import (  # noqa: F401
    ApiTypeError, ModelComposed, ModelNormal, ModelSimple, cached_property,
    change_keys_js_to_python, convert_js_args_to_python_args, date, datetime,
    file_type, none_type, validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from ynab_api.exceptions import ApiAttributeError


class Category(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('goal_type', ): {
            'TB': "TB",
            'TBD': "TBD",
            'MF': "MF",
            'NEED': "NEED",
        },
    }

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'id': (str, ),  # noqa: E501
            'category_group_id': (str, ),  # noqa: E501
            'name': (str, ),  # noqa: E501
            'hidden': (bool, ),  # noqa: E501
            'budgeted': (int, ),  # noqa: E501
            'activity': (int, ),  # noqa: E501
            'balance': (int, ),  # noqa: E501
            'deleted': (bool, ),  # noqa: E501
            'original_category_group_id': (str, ),  # noqa: E501
            'note': (
                str,
                none_type,
            ),  # noqa: E501
            'goal_type': (str, ),  # noqa: E501
            'goal_creation_month': (date, ),  # noqa: E501
            'goal_target': (int, ),  # noqa: E501
            'goal_target_month': (date, ),  # noqa: E501
            'goal_percentage_complete': (int, ),  # noqa: E501
            'goal_months_to_budget': (int, ),  # noqa: E501
            'goal_under_funded': (int, ),  # noqa: E501
            'goal_overall_funded': (int, ),  # noqa: E501
            'goal_overall_left': (int, ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'id': 'id',  # noqa: E501
        'category_group_id': 'category_group_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'hidden': 'hidden',  # noqa: E501
        'budgeted': 'budgeted',  # noqa: E501
        'activity': 'activity',  # noqa: E501
        'balance': 'balance',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'original_category_group_id':
        'original_category_group_id',  # noqa: E501
        'note': 'note',  # noqa: E501
        'goal_type': 'goal_type',  # noqa: E501
        'goal_creation_month': 'goal_creation_month',  # noqa: E501
        'goal_target': 'goal_target',  # noqa: E501
        'goal_target_month': 'goal_target_month',  # noqa: E501
        'goal_percentage_complete': 'goal_percentage_complete',  # noqa: E501
        'goal_months_to_budget': 'goal_months_to_budget',  # noqa: E501
        'goal_under_funded': 'goal_under_funded',  # noqa: E501
        'goal_overall_funded': 'goal_overall_funded',  # noqa: E501
        'goal_overall_left': 'goal_overall_left',  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, category_group_id, name, hidden, budgeted,
                           activity, balance, deleted, *args,
                           **kwargs):  # noqa: E501
        """Category - a model defined in OpenAPI

        Args:
            id (str):
            category_group_id (str):
            name (str):
            hidden (bool): Whether or not the category is hidden
            budgeted (int): Budgeted amount in milliunits format
            activity (int): Activity amount in milliunits format
            balance (int): Balance in milliunits format
            deleted (bool): Whether or not the category has been deleted.  Deleted categories will only be included in delta requests.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            original_category_group_id (str): If category is hidden this is the id of the category group it originally belonged to before it was hidden.. [optional]  # noqa: E501
            note (str, none_type): [optional]  # noqa: E501
            goal_type (str): The type of goal, if the category has a goal (TB='Target Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending'). [optional]  # noqa: E501
            goal_creation_month (date): The month a goal was created. [optional]  # noqa: E501
            goal_target (int): The goal target amount in milliunits. [optional]  # noqa: E501
            goal_target_month (date): The original target month for the goal to be completed.  Only some goal types specify this date.. [optional]  # noqa: E501
            goal_percentage_complete (int): The percentage completion of the goal. [optional]  # noqa: E501
            goal_months_to_budget (int): The number of months, including the current month, left in the current goal period.. [optional]  # noqa: E501
            goal_under_funded (int): The amount of funding still needed in the current month to stay on track towards completing the goal within the current goal period.  This amount will generally correspond to the 'Underfunded' amount in the web and mobile clients except when viewing a category with a Needed for Spending Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when viewing category with a Needed for Spending Goal in a future month.. [optional]  # noqa: E501
            goal_overall_funded (int): The total amount funded towards the goal within the current goal period.. [optional]  # noqa: E501
            goal_overall_left (int): The amount of funding still needed to complete the goal within the current goal period.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__, ),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (
            self.__class__, )

        self.id = id
        self.category_group_id = category_group_id
        self.name = name
        self.hidden = hidden
        self.budgeted = budgeted
        self.activity = activity
        self.balance = balance
        self.deleted = deleted
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, category_group_id, name, hidden, budgeted, activity,
                 balance, deleted, *args, **kwargs):  # noqa: E501
        """Category - a model defined in OpenAPI

        Args:
            id (str):
            category_group_id (str):
            name (str):
            hidden (bool): Whether or not the category is hidden
            budgeted (int): Budgeted amount in milliunits format
            activity (int): Activity amount in milliunits format
            balance (int): Balance in milliunits format
            deleted (bool): Whether or not the category has been deleted.  Deleted categories will only be included in delta requests.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            original_category_group_id (str): If category is hidden this is the id of the category group it originally belonged to before it was hidden.. [optional]  # noqa: E501
            note (str, none_type): [optional]  # noqa: E501
            goal_type (str): The type of goal, if the category has a goal (TB='Target Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending'). [optional]  # noqa: E501
            goal_creation_month (date): The month a goal was created. [optional]  # noqa: E501
            goal_target (int): The goal target amount in milliunits. [optional]  # noqa: E501
            goal_target_month (date): The original target month for the goal to be completed.  Only some goal types specify this date.. [optional]  # noqa: E501
            goal_percentage_complete (int): The percentage completion of the goal. [optional]  # noqa: E501
            goal_months_to_budget (int): The number of months, including the current month, left in the current goal period.. [optional]  # noqa: E501
            goal_under_funded (int): The amount of funding still needed in the current month to stay on track towards completing the goal within the current goal period.  This amount will generally correspond to the 'Underfunded' amount in the web and mobile clients except when viewing a category with a Needed for Spending Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when viewing category with a Needed for Spending Goal in a future month.. [optional]  # noqa: E501
            goal_overall_funded (int): The total amount funded towards the goal within the current goal period.. [optional]  # noqa: E501
            goal_overall_left (int): The amount of funding still needed to complete the goal within the current goal period.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__, ),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (
            self.__class__, )

        self.id = id
        self.category_group_id = category_group_id
        self.name = name
        self.hidden = hidden
        self.budgeted = budgeted
        self.activity = activity
        self.balance = balance
        self.deleted = deleted
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes.")
