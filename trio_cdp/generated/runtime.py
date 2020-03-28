# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.runtime
from cdp.runtime import (
    BindingCalled,
    CallArgument,
    CallFrame,
    ConsoleAPICalled,
    CustomPreview,
    EntryPreview,
    ExceptionDetails,
    ExceptionRevoked,
    ExceptionThrown,
    ExecutionContextCreated,
    ExecutionContextDescription,
    ExecutionContextDestroyed,
    ExecutionContextId,
    ExecutionContextsCleared,
    InspectRequested,
    InternalPropertyDescriptor,
    ObjectPreview,
    PrivatePropertyDescriptor,
    PropertyDescriptor,
    PropertyPreview,
    RemoteObject,
    RemoteObjectId,
    ScriptId,
    StackTrace,
    StackTraceId,
    TimeDelta,
    Timestamp,
    UniqueDebuggerId,
    UnserializableValue
)


async def add_binding(
        name: str,
        execution_context_id: typing.Optional[ExecutionContextId] = None
    ) -> None:
    '''
    If executionContextId is empty, adds binding with the given name on the
    global objects of all inspected contexts, including those created later,
    bindings survive reloads.
    If executionContextId is specified, adds binding only on global object of
    given execution context.
    Binding function takes exactly one argument, this argument should be string,
    in case of any other input, function throws an exception.
    Each binding function call produces Runtime.bindingCalled notification.

    **EXPERIMENTAL**

    :param name:
    :param execution_context_id: *(Optional)*
    '''
    session = get_session_context('runtime.add_binding')
    return await session.execute(cdp.runtime.add_binding(name, execution_context_id))


async def await_promise(
        promise_object_id: RemoteObjectId,
        return_by_value: typing.Optional[bool] = None,
        generate_preview: typing.Optional[bool] = None
    ) -> typing.Tuple[RemoteObject, typing.Optional[ExceptionDetails]]:
    '''
    Add handler to promise with given promise object id.

    :param promise_object_id: Identifier of the promise.
    :param return_by_value: *(Optional)* Whether the result is expected to be a JSON object that should be sent by value.
    :param generate_preview: *(Optional)* Whether preview should be generated for the result.
    :returns: A tuple with the following items:

        0. **result** – Promise result. Will contain rejected value if promise was rejected.
        1. **exceptionDetails** – *(Optional)* Exception details if stack strace is available.
    '''
    session = get_session_context('runtime.await_promise')
    return await session.execute(cdp.runtime.await_promise(promise_object_id, return_by_value, generate_preview))


async def call_function_on(
        function_declaration: str,
        object_id: typing.Optional[RemoteObjectId] = None,
        arguments: typing.Optional[typing.List[CallArgument]] = None,
        silent: typing.Optional[bool] = None,
        return_by_value: typing.Optional[bool] = None,
        generate_preview: typing.Optional[bool] = None,
        user_gesture: typing.Optional[bool] = None,
        await_promise: typing.Optional[bool] = None,
        execution_context_id: typing.Optional[ExecutionContextId] = None,
        object_group: typing.Optional[str] = None
    ) -> typing.Tuple[RemoteObject, typing.Optional[ExceptionDetails]]:
    '''
    Calls function with given declaration on the given object. Object group of the result is
    inherited from the target object.

    :param function_declaration: Declaration of the function to call.
    :param object_id: *(Optional)* Identifier of the object to call function on. Either objectId or executionContextId should be specified.
    :param arguments: *(Optional)* Call arguments. All call arguments must belong to the same JavaScript world as the target object.
    :param silent: *(Optional)* In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides ```setPauseOnException```` state.
    :param return_by_value: *(Optional)* Whether the result is expected to be a JSON object which should be sent by value.
    :param generate_preview: **(EXPERIMENTAL)** *(Optional)* Whether preview should be generated for the result.
    :param user_gesture: *(Optional)* Whether execution should be treated as initiated by user in the UI.
    :param await_promise: *(Optional)* Whether execution should ````await``` for resulting value and return once awaited promise is resolved.
    :param execution_context_id: *(Optional)* Specifies execution context which global object will be used to call function on. Either executionContextId or objectId should be specified.
    :param object_group: *(Optional)* Symbolic group name that can be used to release multiple objects. If objectGroup is not specified and objectId is, objectGroup will be inherited from object.
    :returns: A tuple with the following items:

        0. **result** – Call result.
        1. **exceptionDetails** – *(Optional)* Exception details.
    '''
    session = get_session_context('runtime.call_function_on')
    return await session.execute(cdp.runtime.call_function_on(function_declaration, object_id, arguments, silent, return_by_value, generate_preview, user_gesture, await_promise, execution_context_id, object_group))


async def compile_script(
        expression: str,
        source_url: str,
        persist_script: bool,
        execution_context_id: typing.Optional[ExecutionContextId] = None
    ) -> typing.Tuple[typing.Optional[ScriptId], typing.Optional[ExceptionDetails]]:
    '''
    Compiles expression.

    :param expression: Expression to compile.
    :param source_url: Source url to be set for the script.
    :param persist_script: Specifies whether the compiled script should be persisted.
    :param execution_context_id: *(Optional)* Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
    :returns: A tuple with the following items:

        0. **scriptId** – *(Optional)* Id of the script.
        1. **exceptionDetails** – *(Optional)* Exception details.
    '''
    session = get_session_context('runtime.compile_script')
    return await session.execute(cdp.runtime.compile_script(expression, source_url, persist_script, execution_context_id))


async def disable() -> None:
    '''
    Disables reporting of execution contexts creation.
    '''
    session = get_session_context('runtime.disable')
    return await session.execute(cdp.runtime.disable())


async def discard_console_entries() -> None:
    '''
    Discards collected exceptions and console API calls.
    '''
    session = get_session_context('runtime.discard_console_entries')
    return await session.execute(cdp.runtime.discard_console_entries())


async def enable() -> None:
    '''
    Enables reporting of execution contexts creation by means of ``executionContextCreated`` event.
    When the reporting gets enabled the event will be sent immediately for each existing execution
    context.
    '''
    session = get_session_context('runtime.enable')
    return await session.execute(cdp.runtime.enable())


async def evaluate(
        expression: str,
        object_group: typing.Optional[str] = None,
        include_command_line_api: typing.Optional[bool] = None,
        silent: typing.Optional[bool] = None,
        context_id: typing.Optional[ExecutionContextId] = None,
        return_by_value: typing.Optional[bool] = None,
        generate_preview: typing.Optional[bool] = None,
        user_gesture: typing.Optional[bool] = None,
        await_promise: typing.Optional[bool] = None,
        throw_on_side_effect: typing.Optional[bool] = None,
        timeout: typing.Optional[TimeDelta] = None
    ) -> typing.Tuple[RemoteObject, typing.Optional[ExceptionDetails]]:
    '''
    Evaluates expression on global object.

    :param expression: Expression to evaluate.
    :param object_group: *(Optional)* Symbolic group name that can be used to release multiple objects.
    :param include_command_line_api: *(Optional)* Determines whether Command Line API should be available during the evaluation.
    :param silent: *(Optional)* In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides ```setPauseOnException```` state.
    :param context_id: *(Optional)* Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
    :param return_by_value: *(Optional)* Whether the result is expected to be a JSON object that should be sent by value.
    :param generate_preview: **(EXPERIMENTAL)** *(Optional)* Whether preview should be generated for the result.
    :param user_gesture: *(Optional)* Whether execution should be treated as initiated by user in the UI.
    :param await_promise: *(Optional)* Whether execution should ````await``` for resulting value and return once awaited promise is resolved.
    :param throw_on_side_effect: **(EXPERIMENTAL)** *(Optional)* Whether to throw an exception if side effect cannot be ruled out during evaluation.
    :param timeout: **(EXPERIMENTAL)** *(Optional)* Terminate execution after timing out (number of milliseconds).
    :returns: A tuple with the following items:

        0. **result** – Evaluation result.
        1. **exceptionDetails** – *(Optional)* Exception details.
    '''
    session = get_session_context('runtime.evaluate')
    return await session.execute(cdp.runtime.evaluate(expression, object_group, include_command_line_api, silent, context_id, return_by_value, generate_preview, user_gesture, await_promise, throw_on_side_effect, timeout))


async def get_heap_usage() -> typing.Tuple[float, float]:
    '''
    Returns the JavaScript heap usage.
    It is the total usage of the corresponding isolate not scoped to a particular Runtime.

    **EXPERIMENTAL**

    :returns: A tuple with the following items:

        0. **usedSize** – Used heap size in bytes.
        1. **totalSize** – Allocated heap size in bytes.
    '''
    session = get_session_context('runtime.get_heap_usage')
    return await session.execute(cdp.runtime.get_heap_usage())


async def get_isolate_id() -> str:
    '''
    Returns the isolate id.

    **EXPERIMENTAL**

    :returns: The isolate id.
    '''
    session = get_session_context('runtime.get_isolate_id')
    return await session.execute(cdp.runtime.get_isolate_id())


async def get_properties(
        object_id: RemoteObjectId,
        own_properties: typing.Optional[bool] = None,
        accessor_properties_only: typing.Optional[bool] = None,
        generate_preview: typing.Optional[bool] = None
    ) -> typing.Tuple[typing.List[PropertyDescriptor], typing.Optional[typing.List[InternalPropertyDescriptor]], typing.Optional[typing.List[PrivatePropertyDescriptor]], typing.Optional[ExceptionDetails]]:
    '''
    Returns properties of a given object. Object group of the result is inherited from the target
    object.

    :param object_id: Identifier of the object to return properties for.
    :param own_properties: *(Optional)* If true, returns properties belonging only to the element itself, not to its prototype chain.
    :param accessor_properties_only: **(EXPERIMENTAL)** *(Optional)* If true, returns accessor properties (with getter/setter) only; internal properties are not returned either.
    :param generate_preview: **(EXPERIMENTAL)** *(Optional)* Whether preview should be generated for the results.
    :returns: A tuple with the following items:

        0. **result** – Object properties.
        1. **internalProperties** – *(Optional)* Internal object properties (only of the element itself).
        2. **privateProperties** – *(Optional)* Object private properties.
        3. **exceptionDetails** – *(Optional)* Exception details.
    '''
    session = get_session_context('runtime.get_properties')
    return await session.execute(cdp.runtime.get_properties(object_id, own_properties, accessor_properties_only, generate_preview))


async def global_lexical_scope_names(
        execution_context_id: typing.Optional[ExecutionContextId] = None
    ) -> typing.List[str]:
    '''
    Returns all let, const and class variables from global scope.

    :param execution_context_id: *(Optional)* Specifies in which execution context to lookup global scope variables.
    :returns: 
    '''
    session = get_session_context('runtime.global_lexical_scope_names')
    return await session.execute(cdp.runtime.global_lexical_scope_names(execution_context_id))


async def query_objects(
        prototype_object_id: RemoteObjectId,
        object_group: typing.Optional[str] = None
    ) -> RemoteObject:
    '''
    :param prototype_object_id: Identifier of the prototype to return objects for.
    :param object_group: *(Optional)* Symbolic group name that can be used to release the results.
    :returns: Array with objects.
    '''
    session = get_session_context('runtime.query_objects')
    return await session.execute(cdp.runtime.query_objects(prototype_object_id, object_group))


async def release_object(
        object_id: RemoteObjectId
    ) -> None:
    '''
    Releases remote object with given id.

    :param object_id: Identifier of the object to release.
    '''
    session = get_session_context('runtime.release_object')
    return await session.execute(cdp.runtime.release_object(object_id))


async def release_object_group(
        object_group: str
    ) -> None:
    '''
    Releases all remote objects that belong to a given group.

    :param object_group: Symbolic object group name.
    '''
    session = get_session_context('runtime.release_object_group')
    return await session.execute(cdp.runtime.release_object_group(object_group))


async def remove_binding(
        name: str
    ) -> None:
    '''
    This method does not remove binding function from global object but
    unsubscribes current runtime agent from Runtime.bindingCalled notifications.

    **EXPERIMENTAL**

    :param name:
    '''
    session = get_session_context('runtime.remove_binding')
    return await session.execute(cdp.runtime.remove_binding(name))


async def run_if_waiting_for_debugger() -> None:
    '''
    Tells inspected instance to run if it was waiting for debugger to attach.
    '''
    session = get_session_context('runtime.run_if_waiting_for_debugger')
    return await session.execute(cdp.runtime.run_if_waiting_for_debugger())


async def run_script(
        script_id: ScriptId,
        execution_context_id: typing.Optional[ExecutionContextId] = None,
        object_group: typing.Optional[str] = None,
        silent: typing.Optional[bool] = None,
        include_command_line_api: typing.Optional[bool] = None,
        return_by_value: typing.Optional[bool] = None,
        generate_preview: typing.Optional[bool] = None,
        await_promise: typing.Optional[bool] = None
    ) -> typing.Tuple[RemoteObject, typing.Optional[ExceptionDetails]]:
    '''
    Runs script with given id in a given context.

    :param script_id: Id of the script to run.
    :param execution_context_id: *(Optional)* Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
    :param object_group: *(Optional)* Symbolic group name that can be used to release multiple objects.
    :param silent: *(Optional)* In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides ```setPauseOnException```` state.
    :param include_command_line_api: *(Optional)* Determines whether Command Line API should be available during the evaluation.
    :param return_by_value: *(Optional)* Whether the result is expected to be a JSON object which should be sent by value.
    :param generate_preview: *(Optional)* Whether preview should be generated for the result.
    :param await_promise: *(Optional)* Whether execution should ````await``` for resulting value and return once awaited promise is resolved.
    :returns: A tuple with the following items:

        0. **result** – Run result.
        1. **exceptionDetails** – *(Optional)* Exception details.
    '''
    session = get_session_context('runtime.run_script')
    return await session.execute(cdp.runtime.run_script(script_id, execution_context_id, object_group, silent, include_command_line_api, return_by_value, generate_preview, await_promise))


async def set_async_call_stack_depth(
        max_depth: int
    ) -> None:
    '''
    Enables or disables async call stacks tracking.

    :param max_depth: Maximum depth of async call stacks. Setting to ```0``` will effectively disable collecting async call stacks (default).
    '''
    session = get_session_context('runtime.set_async_call_stack_depth')
    return await session.execute(cdp.runtime.set_async_call_stack_depth(max_depth))


async def set_custom_object_formatter_enabled(
        enabled: bool
    ) -> None:
    '''


    **EXPERIMENTAL**

    :param enabled:
    '''
    session = get_session_context('runtime.set_custom_object_formatter_enabled')
    return await session.execute(cdp.runtime.set_custom_object_formatter_enabled(enabled))


async def set_max_call_stack_size_to_capture(
        size: int
    ) -> None:
    '''


    **EXPERIMENTAL**

    :param size:
    '''
    session = get_session_context('runtime.set_max_call_stack_size_to_capture')
    return await session.execute(cdp.runtime.set_max_call_stack_size_to_capture(size))


async def terminate_execution() -> None:
    '''
    Terminate current or next JavaScript execution.
    Will cancel the termination when the outer-most script execution ends.

    **EXPERIMENTAL**
    '''
    session = get_session_context('runtime.terminate_execution')
    return await session.execute(cdp.runtime.terminate_execution())