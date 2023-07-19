import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="RDS-Model-Monitoring",
    page_icon=":bar_chart:",
    layout="wide",   
)

st.title(":bar_chart: RDS Model Accuracy Monitoring")
st.markdown('---')


# Loading the csv into dataframe to be used by streamlit

df= pd.read_csv('DB_Forecast_Monitoring_test.csv')

#adding sidebar to filter instance and date and time
st.sidebar.title("Please filter the instance name, date and time of execution...")
instance_options=['apigw-preview-usw1-apic-rds','apigw-prod-use2-dr-rds-v5737','apigw-prod-use4-dr-rds-v5737','apigw-prod-use6-dr-rds-v5737','apigw-prod-usw5-rds1','apigw-staging-usw1-apic-rds','apigw-staging-usw1-db','apigwdb-florence01','auroraupgrade-2','auroraupgrade-2-instance-1','b2bgw-prod-use2-rds-5734-dr','b2bgw-prod-use6-rds-5734-dr','b2bgw-prod-usw1-rds-5734','b2bgw-prod-usw3-rds-5734','b2bgw-rds-instance-prod-preview-usw1-v5724','b2bgw-rds-instance-prod-use4-5734-dr','b2bgw-rds-instance-prod-usw5','b2bgw-rds-instance-staging-usw1-5734','cai-preview-c360-usw1-process-rds-v5737','cai-preview-usw1-process-rds-v5737','cai-prod-ford-use1-process-rds-dr-v5737','cai-prod-use2-process-rds-dr-v5737','cai-prod-use4-process-rds-dr-v5737','cai-prod-use6-process-rds-dr-v5737','cai-prod-usw1-log-rds-v5737','cai-prod-usw1-process-rds-v5737','cai-prod-usw3-process-log-rds-v5737','cai-prod-usw3-process-rds-v5737','cai-prod-usw5-process-rds-v5737','cai-staging-usw1-process-rds','cai-staging-usw3-process-rds','ccgf-prod-m1-cdgc-mysql','ccgf-prod-m1-cdgc-tds-mysql','ccgf-prod-m1-pltf-mysql','ccgf-staging-mysql','ccgf-staging-tds-mysql','cdi-preview-c360-cms-etl-new','cdi-preview-c360-global-cdiglobal-rds','cdi-preview-c360-ics-etl','cdi-preview-c360-usw1-cdi','cdi-preview-c360-usw1-cdiglobal-db','cdi-preview-us-global-cdiglobal-rds','cdi-preview-us-maids-etl','cdi-preview-usw1-cdi','cdi-preview-usw1-cdi-etl','cdi-preview-usw1-cdiglobal-db','cdi-preview-usw1-cms-etl-new','cdi-preview-usw1-runtime-etl-new','cdi-preview-usw1-saasext','cdi-prod-icinq-cms-etl-new','cdi-prod-icinq-ics-etl','cdi-prod-icinq-runtime-etl-new','cdi-prod-icinq1-usw1-cdi','cdi-prod-maids-etl-new','cdi-prod-us-global-cdiglobal-rds','cdi-prod-use2-cdi-m2m-dr','cdi-prod-use2-ford-ics-m2m-dr','cdi-prod-use4-cdi-m2m-dr','cdi-prod-use6-cdi-m2m-dr','cdi-prod-usw1-cdi-etl','cdi-prod-usw1-cdiglobal-db','cdi-prod-usw1-cdiinsights-etl', 'cdi-prod-usw1-cms-etl', 'cdi-prod-usw1-frs-etl', 'cdi-prod-usw1-ics-log-etl-new', 'cdi-prod-usw1-runtime-etl-new', 'cdi-prod-usw1-saasext-new', 'cdi-prod-usw1-svc-etl', 'cdi-prod-usw3-cdi', 'cdi-prod-usw3-cdiglobal-db', 'cdi-prod-usw3-cdiinsights-etl', 'cdi-prod-usw3-cms-etl', 'cdi-prod-usw3-frs-new-etl', 'cdi-prod-usw3-ics-log-etl-new', 'cdi-prod-usw3-runtime-new-etl', 'cdi-prod-usw3-saasext-new', 'cdi-prod-usw3-svc-etl', 'cdi-prod-usw5-cdiglobal-db', 'cdi-prod-usw5-cdiinsights-etl', 'cdi-prod-usw5-cms-new-etl', 'cdi-prod-usw5-frs-new-etl', 'cdi-prod-usw5-ics-log-etl', 'cdi-prod-usw5-runtime-new-etl', 'cdi-prod-usw5-saasext', 'cdi-prod-usw5-svc-etl', 'cdi-prod1-ics-app-mysql8test', 'cdi-prod1-ics-log-mysql8test', 'cdi-staging-us-global-cdiglobal-rds', 'cdi-staging-usw1-cdi', 'cdi-staging-usw1-cdiglobal-db', 'cdi-staging-usw1-saasext', 'cdi-staging-usw3-cdi', 'cdi-use2-svc-5724-dr-m2m', 'cdipc-preview-usw1-rds', 'cdipc-staging-usw1-rds', 'cdv-preview-usw1-rds', 'cdv-prod-icinq1-usw1-rds', 'cdv-staging-usw1-rds', 'cihdb-pod4-florence01-dr', 'cihdb-pod6-master-dr', 'cihdb-prod-use2-mysql-dr-replica', 'cihdb-prod-usw1-mysql', 'cihdb-prod-usw3-master', 'cihdb-prod-usw5-aurora', 'cihdb-prod-usw5-aurora-1', 'cihdb-prod-usw5-aurora-2', 'cihdb-prod-usw5-mysql-master', 'cihdb-use2-prod-aurora-dr-cluster-1', 'cihdb-use2-prod-aurora-dr-instance-1', 'cihdb-use4-prod-aurora-dr-cluster-1', 'cihdb-use4-prod-aurora-dr-instance-1', 'cihdb-use6-prod-aurora-dr-cluster-1', 'cihdb-use6-prod-aurora-dr-instance-1', 'cihdb-usw1-preview', 'cihdb-usw1-preview-prod-aurora', 'cihdb-usw1-preview-prod-aurora-1','cihdb-usw1-preview-prod-aurora-2', 'cihdb-usw1-prod-aurora', 'cihdb-usw1-prod-aurora-1', 'cihdb-usw1-prod-aurora-2', 'cihdb-usw1-staging-mysql', 'cihdb-usw1-staging-prod-aurora', 'cihdb-usw1-staging-prod-aurora-instance-1', 'cihdb-usw1-staging-prod-aurora-instance-1-us-west-2a', 'cihdb-usw3-prod-aurora', 'cihdb-usw3-prod-aurora-1', 'cihdb-usw3-prod-aurora-2', 'database-1', 'disn-preview-c360-usw1-rds', 'disn-prod-use4-rds-dr-replica', 'disn-prod-usw3-disn-rds', 'disn-staging-usw1-rds-rollback', 'dqcloud-c360-dictionary-1', 'dqcloud-c360-modelstore-1', 'dqcloud-icinq1-dictionary-1', 'dqcloud-icinq1-modelstore-1', 'dqcloud-na2dr-dictionary-1', 'dqcloud-na2dr-modelstore-1', 'dqcloud-prerel-dictionary-1', 'dqcloud-prerel-modelstore-1', 'dqcloud-use4dr-dictionary-1', 'dqcloud-use4dr-modelstore-1', 'dqcloud-use6dr-dictionary-1', 'dqcloud-use6dr-modelstore-1', 'dqcloud-usw1-dictionary-1', 'dqcloud-usw1-modelstore-1', 'dqcloud-usw1stg-dictionary-1', 'dqcloud-usw1stg-modelstore-1', 'dqcloud-usw3-dictionary-1', 'dqcloud-usw3-modelstore-1', 'dqcloud-usw5-dictionary-1', 'dqcloud-usw5-modelstore-1', 'dqprofiling-c360-metric-store', 'dqprofiling-c360-metric-store-0', 'dqprofiling-c360-metric-store-1', 'dqprofiling-c360-profilingservice-1', 'dqprofiling-na2dr-metric-store', 'dqprofiling-na2dr-metric-store-0', 'dqprofiling-na2dr-profilingservice-1', 'dqprofiling-prerel-metric-store', 'dqprofiling-prerel-metric-store-0', 'dqprofiling-prerel-metric-store-1', 'dqprofiling-prerel-profilingservice-1', 'dqprofiling-use4dr-metric-store', 'dqprofiling-use4dr-metric-store-0', 'dqprofiling-use4dr-profilingservice-1', 'dqprofiling-use6dr-metric-store', 'dqprofiling-use6dr-metric-store-0', 'dqprofiling-use6dr-profilingservice-1', 'dqprofiling-usw1-metric-store', 'dqprofiling-usw1-metric-store-us-west-2a', 'dqprofiling-usw1-metric-store-us-west-2b', 'dqprofiling-usw1-profilingservice-1', 'dqprofiling-usw1stg-metric-store', 'dqprofiling-usw1stg-metric-store-0','dqprofiling-usw1stg-profilingservice-2', 'dqprofiling-usw3-metric-store', 'dqprofiling-usw3-metric-store-0', 'dqprofiling-usw3-metric-store-1', 'dqprofiling-usw3-profilingservice-1', 'dqprofiling-usw5-metric-store', 'dqprofiling-usw5-metric-store-0', 'dqprofiling-usw5-metric-store-1', 'dqprofiling-usw5-profilingservice-1', 'gcsassure-prod-r35-cluster', 'gcsassure-prod-stage-202210m', 'ias-preview-usw1-rds', 'ias-prod-use2-rds-dr-replica', 'ias-prod-use4-rds-dr-replica', 'ias-prod-use6-rds-dr-replica', 'ias-prod-usw1-rds', 'ias-prod-usw3-rds', 'ias-prod-usw5-rds', 'ias-staging-usw1-rds-rollback', 'idmcp-staging-us-mysql', 'iics-c360-usw1-ics', 'iics-deloitte-ics-app-m2m-dr', 'iics-deloitte-ics-log-m2m-dr', 'iics-deloitte-svc-m2m-dr', 'iics-dmstaging-usw1-ics-app-m2m', 'iics-icinq1-ics-5724', 'iics-preview-c360-ids-ids-v5737-db', 'iics-preview-c360-usw1-cms-v5737-db', 'iics-preview-c360-usw1-runtime-v5737-db', 'iics-preview-maids-ids-v5737-db', 'iics-preview-usw1-cms-v5737-db', 'iics-preview-usw1-runtime-v5737-db', 'iics-prod-ford-use1dr-cms-v5737-drdb', 'iics-prod-ford-use1dr-runtime-v5737-drdb', 'iics-prod-icinq1-usw1-cms-v5737-db', 'iics-prod-icinq1-usw1-runtime-v5737-db', 'iics-prod-maids-ids-v5737-db', 'iics-prod-maids-pkgmgr-v5737-db', 'iics-prod-pdel-idsdr-ids-v5737-drdb', 'iics-prod-pdel-idsdr-pkgmgr-v5737-drdb', 'iics-prod-pdel-poddr-cms-v5737-drdb', 'iics-prod-pdel-poddr-frs-v5737-drdb', 'iics-prod-pdel-poddr-runtime-v5737-drdb', 'iics-prod-pod3-apigw-rds', 'iics-prod-use2dr-cms-v5737-drdb', 'iics-prod-use2dr-frs-v5737-drdb', 'iics-prod-use2dr-kms-v5737-drdb', 'iics-prod-use2dr-runtime-v5737-drdb', 'iics-prod-use4dr-cms-v5737-drdb', 'iics-prod-use4dr-frs-v5737-drdb', 'iics-prod-use4dr-kms-v5737-drdb', 'iics-prod-use4dr-runtime-v5737-drdb','iics-prod-use6dr-cms-v5737-drdb', 'iics-prod-use6dr-frs-v5737-drdb', 'iics-prod-use6dr-kms-v5737-drdb', 'iics-prod-use6dr-runtime-v5737-drdb', 'iics-prod-usw1-cdi', 'iics-prod-usw1-cms-v5737-db', 'iics-prod-usw1-frs-v5737-db', 'iics-prod-usw1-kms-v5737-db', 'iics-prod-usw1-runtime-v5737-db', 'iics-prod-usw1-runtime-v5737-db-opsinsight-replica', 'iics-prod-usw3-cms-v5737-db', 'iics-prod-usw3-frs-v5737-db', 'iics-prod-usw3-kms-v5737-db', 'iics-prod-usw3-runtime-v5737-db', 'iics-prod-usw3-runtime-v5737-db-opsinsight-replica', 'iics-prod-usw5-cms-v5737-db', 'iics-prod-usw5-frs-v5737-db', 'iics-prod-usw5-kms-v5737-db', 'iics-prod-usw5-runtime-v5737-db', 'iics-prod-usw5-runtime-v5737-db-opsinsight-replica', 'iics-prod1-ics-app-5724', 'iics-prod1-ics-log-5724', 'iics-prod1-ms-cdiinsights', 'iics-prod1-ms-pc2cloud-5724', 'iics-prod1-ms-svc-5724', 'iics-sl-us-serverless-cdi', 'iics-staging-maids-ids-v5737-db', 'iics-staging-sl-us-sl-rds', 'iics-staging-usw1-cms-v5737-db', 'iics-staging-usw1-runtime-v5737-db', 'iics-staging-usw1-runtime-v5737-db-opsinsight-replica', 'iics-staging-usw3-ics-rds', 'iics-use2-cdiinsights-m2m-dr', 'iics-use2-ics-app-5724-m2m-dr', 'iics-use2-ics-log-5724-m2m-dr', 'iics-use2-pc2cloud-5724-m2m-dr', 'iics-use2-svc-5724-m2m-dr', 'iics-use4-cdiinsights-m2m-dr', 'iics-use4-ics-app-5724-m2m-dr', 'iics-use4-ics-log-5724-m2m-dr', 'iics-use4-pc2cloud-5724-m2m-dr', 'iics-use4-svc-5724-m2m-dr', 'iics-use6-cdiinsights-m2m-dr', 'iics-use6-ics-app-5724-m2m-dr', 'iics-use6-ics-log-5724-m2m-dr', 'iics-use6-pc2cloud-5724-m2m-dr', 'iics-use6-svc-5724-m2m-dr', 'iics-usw1-preview-apigw-rds-v5724-replica', 'iics-usw1-preview-ics-rds','iics-usw3-cdiinsights', 'iics-usw3-ics-app-5724', 'iics-usw3-ics-log-5724', 'iics-usw3-pc2cloud-5724', 'iics-usw3-service-5724', 'iics-usw5-cdiinsights', 'iics-usw5-ics-app', 'iics-usw5-ics-log', 'iics-usw5-pc2cloud', 'iics-usw5-svc', 'opsinsight-prod-ext-usedr-db-8-0-28', 'opsinsight-prod-ext-usw-db-8-0-28', 'opsinsight-staging-ext-usw-aurora-rds', 'opsinsight-staging-ext-usw-aurora-rds-1', 'opsinsight-staging-ext-usw-db-8-0-28', 'opsinsights-rds-aurora-cluster-prod-ext-usedr', 'opsinsights-rds-aurora-cluster-prod-ext-usw', 'opsinsights-rds-aurora-instance-prod-ext-usedr-1', 'opsinsights-rds-aurora-instance-prod-ext-usw-0', 'opsinsights-rds-aurora-instance-prod-ext-usw-1', 'sl-preview-sl-us-agmr-db', 'sl-preview-sl-us-wps-db', 'sl-preview-sl-us-wps-db-replica', 'sl-prod-sl-us-db', 'sl-prod-sl-us-db-replica', 'sl-warmpool-staging-sl-us-db-rollback', 'sl-warmpool-staging-sl-us-db-rollback-sos-replica', 'taskflow-preview-c360-usw1-process-rds-v5737', 'taskflow-preview-usw1-process-rds-v5737', 'taskflow-prod-deloitte-process-rds-dr-v5737', 'taskflow-prod-ford-process-rds-dr-v5737', 'taskflow-prod-icinq1-usw1-process-rds-v5737', 'taskflow-prod-use2-process-rds-dr-v5737', 'taskflow-prod-use4-process-rds-dr-v5737', 'taskflow-prod-use6-process-rds-dr-v5737', 'taskflow-prod-usw1-log-rds-v5737', 'taskflow-prod-usw1-process-rds-v5737', 'taskflow-prod-usw3-process-log-rds-v5737', 'taskflow-prod-usw3-process-rds-v5737', 'taskflow-prod-usw5-process-log-rds-v5737', 'taskflow-prod-usw5-process-rds-v5737', 'taskflow-staging-usw1-process-rds']

instance=st.sidebar.selectbox(
    "Select the instance:-",
    instance_options,
    index=0
)

instance_forecasted=instance+"_Forecasted"
instance_threshold=instance+"_Threshold"


#Gettting range of date and time to plot graph between actual and forecasted values
date_left_range=st.sidebar.selectbox(
    "Select from which date and time to plot the graph:",
    options=df['date'].unique(),
    index=5
)

date_right_range=st.sidebar.selectbox(
    "Select to which date and time to plot the graph:",
    options=df['date'].unique(),
    index=10
)



left_column,middle_column,right_column=st.columns(3)
with left_column:
    st.subheader("Current Instance:")
    st.subheader(instance)
with middle_column:
    st.subheader("From:")
    st.subheader(date_left_range)
with right_column:
    st.subheader("To:")
    st.subheader(date_right_range)

st.markdown("---")


left_index=df.index[df['date']==date_left_range][0]
right_index=df.index[df['date']==date_right_range][0]
df_plot=df.loc[left_index:right_index, :].sort_values('date')

df_main=df_plot[['date',instance,instance_forecasted,instance_threshold]]

st.dataframe(df_main)

st.markdown('---')
fig = px.bar(df_plot, x=instance, y='date', color=instance_forecasted, title='Graph between actual and forecasted values:-', labels={'column1':'X-axis Label', 'column2':'Y-axis Label', 'date_time':'Date Time'})
# fig.show()

st.plotly_chart(fig)

# ----- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
