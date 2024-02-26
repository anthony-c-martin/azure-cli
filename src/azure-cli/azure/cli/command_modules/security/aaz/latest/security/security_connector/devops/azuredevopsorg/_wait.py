# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "security security-connector devops azuredevopsorg wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.security/securityconnectors/{}/devops/default/azuredevopsorgs/{}", "2023-09-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.org_name = AAZStrArg(
            options=["--org-name"],
            help="The Azure DevOps organization name.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.security_connector_name = AAZStrArg(
            options=["-n", "--name", "--security-connector-name"],
            help="The security connector name.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AzureDevOpsOrgsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class AzureDevOpsOrgsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName}/devops/default/azureDevOpsOrgs/{orgName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "orgName", self.ctx.args.org_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "securityConnectorName", self.ctx.args.security_connector_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.actionable_remediation = AAZObjectType(
                serialized_name="actionableRemediation",
            )
            properties.onboarding_state = AAZStrType(
                serialized_name="onboardingState",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.provisioning_status_message = AAZStrType(
                serialized_name="provisioningStatusMessage",
                flags={"read_only": True},
            )
            properties.provisioning_status_update_time_utc = AAZStrType(
                serialized_name="provisioningStatusUpdateTimeUtc",
                flags={"read_only": True},
            )

            actionable_remediation = cls._schema_on_200.properties.actionable_remediation
            actionable_remediation.branch_configuration = AAZObjectType(
                serialized_name="branchConfiguration",
            )
            actionable_remediation.category_configurations = AAZListType(
                serialized_name="categoryConfigurations",
            )
            actionable_remediation.inherit_from_parent_state = AAZStrType(
                serialized_name="inheritFromParentState",
            )
            actionable_remediation.state = AAZStrType()

            branch_configuration = cls._schema_on_200.properties.actionable_remediation.branch_configuration
            branch_configuration.annotate_default_branch = AAZStrType(
                serialized_name="annotateDefaultBranch",
            )
            branch_configuration.branch_names = AAZListType(
                serialized_name="branchNames",
            )

            branch_names = cls._schema_on_200.properties.actionable_remediation.branch_configuration.branch_names
            branch_names.Element = AAZStrType()

            category_configurations = cls._schema_on_200.properties.actionable_remediation.category_configurations
            category_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.actionable_remediation.category_configurations.Element
            _element.category = AAZStrType()
            _element.minimum_severity_level = AAZStrType(
                serialized_name="minimumSeverityLevel",
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""


__all__ = ["Wait"]
