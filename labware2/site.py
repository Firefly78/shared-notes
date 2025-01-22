from unitelabs.cdk import sila

# Cheat - to make linter happy
HandoverPosition = str
PositionIndex = int
InvalidCommandSequence = Exception
LabwareNotPicked = Exception
LabwareNotPlaced = Exception


class LabwareTransferSiteControllerBase(sila.Feature):
    @sila.ObservableCommand(name="Prepare For Input", errors=[InvalidCommandSequence])
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

    @sila.ObservableCommand(name="Prepare For Output", errors=[InvalidCommandSequence])
    async def PrepareForOutput(
        self,
        HandoverPosition: HandoverPosition,
        InternalPosition: PositionIndex,
        *,
        status: sila.Status,
    ) -> None:
        pass

    @sila.ObservableCommand(name="Labware Delivered", errors=[InvalidCommandSequence])
    async def LabwareDelivered(
        self,
        HandoverPosition: HandoverPosition,
        *,
        status: sila.Status,
    ):
        pass

    @sila.ObservableCommand(name="Labware Removed", errors=[InvalidCommandSequence])
    async def LabwareRemoved(
        self,
        HandoverPosition: HandoverPosition,
        *,
        status: sila.Status,
    ):
        pass

    @sila.UnobservableProperty(display_name="Available Handover Positions")
    async def AvailableHandoverPositions(self) -> list[HandoverPosition]:
        return []

    @sila.UnobservableProperty(display_name="Number Of Internal Positions")
    async def NumberOfInternalPositions(
        self,
    ) -> int:
        return 1
