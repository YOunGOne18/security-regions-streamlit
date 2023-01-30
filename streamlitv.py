import streamlit as st

st.write("""
# Security Tooling Region Check

Select the tools you want to check region compatibility for:

""")

guardduty = st.checkbox("Guardduty")
config = st.checkbox("Config")
ct = st.checkbox("Control Tower")
waf = st.checkbox("WAF")
securityhub = st.checkbox("SecurityHub")
inspectorc = st.checkbox("AWS Inspector Classic")
inspector = st.checkbox("AWS Inspector")
ssm = st.checkbox("SSM")

service_properties = {"guardduty": [{"selected": guardduty, "regions": ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-southeast-3", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-south-1", "eu-west-3", "eu-north-1", "eu-central-2", "me-south-1", "me-central-1", "sa-east-1", "us-gov-east-1", "us-gov-west-1"]}], "config": [{"selected": config, "regions": ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-south-2", "ap-southeast-3", "ap-southeast-4", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-south-1", "eu-west-3", "eu-south-2", "eu-north-1", "eu-central-2", "me-south-1", "me-central-1", "sa-east-1", "us-gov-east-1", "us-gov-west-1"]}], "ct": [{"selected": ct, "regions": ["us-east-1", "us-east-2", "us-west-2", "ca-central-1", "ap-southeast-2", "ap-southeast-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-north-1", "ap-south-1", "ap-northeast-2", "ap-northeast-1", "eu-west-3", "sa-east-1"]}], "waf": [{"selected": waf, "regions": ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-southeast-3", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-south-1", "eu-west-3", "eu-north-1", "me-south-1", "me-central-1", "sa-east-1", "us-gov-east-1", "us-gov-west-1"]}], "securityhub": [{"selected": securityhub, "regions": ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-southeast-3", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-south-1", "eu-west-3", "eu-north-1", "me-south-1", "me-central-1", "sa-east-1", "us-gov-east-1", "us-gov-west-1"]}], "inspectorc": [{"selected": inspectorc, "regions": ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-south-1", "ap-northeast-2", "ap-southeast-2", "ap-northeast-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-north-1", "us-gov-east-1", "us-gov-west-1"]}], "inspector": [{"selected": inspector, "regions": ["us-east-1", "us-east-2", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-south-1", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1", "us-gov-east-1", "us-gov-west-1"]}], "ssm": [{"selected": ssm, "regions": ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-south-2", "ap-southeast-3", "ap-southeast-4", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-south-1", "eu-west-3", "eu-south-2", "eu-north-1", "eu-central-2", "me-south-1", "me-central-1", "sa-east-1", "us-gov-east-1", "us-gov-west-1"]}]}

temp_regions = []
common_regions = []

for selected_service in service_properties:
    if service_properties[selected_service][0]["selected"]:
        if len(temp_regions) == 0:
            for region in service_properties[selected_service][0]["regions"]:
                if region not in common_regions:
                    common_regions.append(region)
                    temp_regions.append(region)
        else:
            common_regions = []
            for region in temp_regions:
                if region in service_properties[selected_service][0]["regions"]:
                    common_regions.append(region)
            temp_regions = common_regions

st.write(common_regions)