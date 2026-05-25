[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "orders_bronze_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared orders_bronze = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "dc024af1-86c0-4c27-a198-8311368df95f"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "88414f66-4801-4d95-ab29-2f77013cb0e9"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "orders_bronze", ItemKind = "Table"]}[Data],
  #"Filtered rows" = Table.SelectRows(#"Navigation 2", each ([order_amount] <> null and [order_amount] <> 0)),
  #"Inserted conditional column" = Table.AddColumn(#"Filtered rows", "revenue_band", each if [order_amount] > 1000 then "High" else "Low"),
  #"Changed column type" = Table.TransformColumnTypes(#"Inserted conditional column", {{"revenue_band", type text}})
in
  #"Changed column type";
shared orders_bronze_DataDestination = let
  Pattern = Lakehouse.Contents([CreateNavigationProperties = false, EnableFolding = false, HierarchicalNavigation = true, EnableVorder = true, OutputMetadataRefresh = true]),
  Navigation_1 = Pattern{[workspaceId = "dc024af1-86c0-4c27-a198-8311368df95f"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "88414f66-4801-4d95-ab29-2f77013cb0e9"]}[Data],
  Navigation_3 = Navigation_2{[Id = "dbo", ItemKind = "Schema"]}[Data],
  TableNavigation = Navigation_3{[Id = "orders_silver", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;
