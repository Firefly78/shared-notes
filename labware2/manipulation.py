from unitelabs.cdk import sila

# Cheat - to make linter happy
HandoverPosition = str
PositionIndex = int
InvalidCommandSequence = Exception
LabwareNotPicked = Exception
LabwareNotPlaced = Exception


class LabwareManipulator(sila.Feature):
    @sila.ObservableCommand(errors=[InvalidCommandSequence])
    async def PrepareForInput(
        self,
        HandoverPosition: HandoverPosition,
        InternalPosition: PositionIndex,
        LabwareType: str,
        LabwareUniqueID: str,
        *,
        status: sila.Status,
    ) -> None:
        pass

    @sila.ObservableCommand(errors=[InvalidCommandSequence])
    async def PrepareForOutput(
        self,
        HandoverPosition: HandoverPosition,
        InternalPosition: PositionIndex,
        *,
        status: sila.Status,
    ) -> None:
        pass

    @sila.ObservableCommand(
        name="Put Labware", errors=[InvalidCommandSequence, LabwareNotPlaced]
    )
    async def PutLabware(
        self,
        HandoverPosition: HandoverPosition,
        IntermediateActions: list[str],
        *,
        status: sila.Status,
    ) -> None:
        pass

    @sila.ObservableCommand(errors=[InvalidCommandSequence, LabwareNotPicked])
    @sila.Response(
        "HandoverPosition", "The position where the labware was retrieved from."
    )
    async def GetLabware(
        self,
        HandoverPosition: HandoverPosition,
        IntermediateActions: list[str],
        *,
        status: sila.Status,
    ) -> HandoverPosition:
        return ""

    @sila.UnobservableProperty(display_name="Available Handover Positions")
    async def AvailableHandoverPositions(self) -> list[HandoverPosition]:
        return []

    @sila.UnobservableProperty(display_name="Number Of Internal Positions")
    async def NumberOfInternalPositions(
        self,
    ) -> int:
        return 1

    @sila.UnobservableProperty(display_name="Available Intermediate Actions")
    async def AvailableIntermediateActions(
        self,
    ) -> list[str]:
        """Returns all commands that can be executed within a "Put Labware" or "Get Labware" command execution."""
        return []
