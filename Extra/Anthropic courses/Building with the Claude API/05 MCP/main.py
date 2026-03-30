import asyncio
import sys
import os
from dotenv import load_dotenv
from contextlib import AsyncExitStack

from mcp_client import MCPClient
from core.claude import Claude

from core.cli_chat import CliChat
from core.cli import CliApp

load_dotenv()

# Anthropic Config
claude_model = os.getenv("CLAUDE_MODEL", "")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "")


assert claude_model, "Error: CLAUDE_MODEL cannot be empty. Update .env"
assert anthropic_api_key, (
    "Error: ANTHROPIC_API_KEY cannot be empty. Update .env"
)


async def main():
    claude_service = Claude(model=claude_model)

    server_scripts = sys.argv[1:]
    clients = {}

    def is_uv_available():
        import shutil
        return shutil.which("uv") is not None

    use_uv = os.getenv("USE_UV", "0") == "1"
    if use_uv and not is_uv_available():
        print("Warning: USE_UV=1 is set but 'uv' was not found. Falling back to 'python'.")
        use_uv = False

    def get_command_args(script):
        return (
            ("uv", ["run", script])
            if use_uv
            else (sys.executable, [script])
        )

    async with AsyncExitStack() as stack:
        cmd, args = get_command_args("mcp_server.py")
        doc_client = await stack.enter_async_context(
            MCPClient(command=cmd, args=args)
        )
        clients["doc_client"] = doc_client

        for i, server_script in enumerate(server_scripts):
            client_id = f"client_{i}_{server_script}"
            script_command, script_args = get_command_args(server_script)
            client = await stack.enter_async_context(
                MCPClient(command=script_command, args=script_args)
            )
            clients[client_id] = client

        chat = CliChat(
            doc_client=doc_client,
            clients=clients,
            claude_service=claude_service,
        )

        cli = CliApp(chat)
        await cli.initialize()
        await cli.run()


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())
